from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, ListView, UpdateView
from django.db import IntegrityError
from tournament.models import Tournament
from .forms import RegisterForm, ChessPlayerForm
from .models import ChessPlayers, Region
from tablib import Dataset


@login_required
def index(request):
    context = {}
    context['header_title'] = 'Главная'
    return render(request, 'players/account.html', context=context)





def check_username(request):
    email = request.POST.get('email')

    query = f"SELECT COUNT(*) FROM players_user WHERE email = '{email}'"
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchone()
        if row[0] > 0:
            return HttpResponse("<div style='color: red;'>Пользователь с такой почтой уже есть</div>")
        else:
            return HttpResponse("<div style='color: green;'>Имя пользователя свободно</div>")





class ChessPlayersListView(ListView):
    template_name = 'players/database.html'
    model = ChessPlayers
    context_object_name = 'players'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'База шахматистов'
        context['sort_status'] = self.request.GET.get('duration')
        context['direction_asc'] = self.request.GET.get('direction')
        context['regions'] = Region.objects.all()
        context['tournaments'] = Tournament.objects.filter(organizer=self.request.user)
        return context

    def get_queryset(self):
        queryset = ChessPlayers.objects.all()
        sort_by = self.request.GET.get('sort_by', 'last_name')  # По умолчанию сортировка по фамилии
        direction = self.request.GET.get('direction', 'asc')  # По умолчанию сортировка по возрастанию

        if direction == 'desc':
            sort_by = '-' + sort_by  # Добавляем "-" для сортировки по убыванию

        return queryset.order_by(sort_by)

    def post(self, request, *args, **kwargs):
        dataset = Dataset()

        if 'myfile' in request.FILES:
            myfile = request.FILES['myfile']
            if myfile.name.endswith('xlsx'):
                imported_data = dataset.load(myfile.read(), format='xlsx')

                for data in imported_data:
                    region = get_object_or_404(Region, title=data[3])
                    try:
                        chess_player = ChessPlayers(
                            fide_id=data[0],
                            last_name=data[1],
                            first_name=data[2],
                            region=region,
                        )
                        chess_player.save()
                    except IntegrityError:
                        continue


                messages.success(request, 'Данные успешно импортированы.')
                return HttpResponseRedirect(reverse('database'))  # Redirect after successful import
            else:
                messages.error(request, 'Формат файла не поддерживается. Используйте файл в формате Excel (XLSX).')
        else:
            messages.error(request, 'Файл не был загружен.')

        # If file upload fails or format is not supported, render the form page again
        return render(request, template_name='players/database.html')  # Return a response in all cases


class ChessPlayersUpdate(UpdateView):
    context_object_name = 'player'
    model = ChessPlayers
    template_name = 'players/detail_chess_player.html'
    fields = ['fide_id', 'title', 'first_name', 'last_name']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Редактирование записи'
        return context


def add_chess_player(request):
    if request.method == "POST":
        form = ChessPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('database'))

    else:
        form = ChessPlayerForm()
    return render(request, 'players/create_chess_player.html', {
        'form': form,
    })


from django.http import QueryDict


def edit_chess_player(request, pk):
    player = get_object_or_404(ChessPlayers, pk=pk)
    if request.method == 'POST':
        # Если запрос инициирован методом PUT, заменяем request.POST на request.PUT
        if request.POST.get('_method') == 'PUT':
            player = get_object_or_404(ChessPlayers, pk=pk)
            player.fide_id = request.POST.get('fide_id')
            player.last_name = request.POST.get('last_name')
            player.first_name = request.POST.get('first_name')
            player.region = request.POST.get('region')
            player.save()

            # Возвращаем JSON-ответ с сообщением об успешном обновлении
            return JsonResponse({'message': 'Player updated successfully'})
        else:
            # В случае других методов запроса возвращаем ошибку метода
            return JsonResponse({'error': 'Method not allowed'}, status=405)
    return render(request, 'players/detail_chess_player.html', context={'player': player})


def get_chess_player(request, pk):
    player = get_object_or_404(ChessPlayers, pk=pk)
    regions = Region.objects.all()
    return render(request, 'players/get_chess_player.html', context={'player': player, 'regions': regions})


def edit_city_record(request, pk):
    print(request.method)
    player = ChessPlayers.objects.get(pk=pk)

    if request.method == 'POST':
        city_form = ChessPlayerForm(request.POST, instance=player)
        print(request.POST.get('fide_id'))
        if city_form.is_valid():
            city_form.save()
        else:
            print(city_form.errors)
    else:
        city_form = ChessPlayerForm(instance=player)
    return render(request, 'players/detail_chess_player.html', context={'player': player})


def delete_chess_player(request, pk):
    player = get_object_or_404(ChessPlayers, pk=pk)
    player.delete()
    page_number = request.GET.get('page', 1)
    players_list = ChessPlayers.objects.all()
    paginator = Paginator(players_list, 5
                          )
    try:
        players = paginator.page(page_number)
    except EmptyPage:
        # Если указанная страница пуста, возвращаем последнюю страницу
        players = paginator.page(paginator.num_pages)

    # Возвращаем обновленный фрагмент таблицы игроков с учетом пагинации
    context = {'players': players}
    return render(request, 'players/partials/chess_player_table.html', context=context)



def search(request):
    field = request.GET.get('field')  # Поле для поиска (fide_id или last_name)
    query = request.GET.get('query')  # Строка поиска
    region = request.GET.get('region')
    players = ChessPlayers.objects.all()

    # Фильтрация по полю поиска и строке поиска
    if field and query:
        if field == 'fide_id':
            players = players.filter(fide_id__icontains=query)
        elif field == 'last_name':
            players = players.filter(last_name__icontains=query)

    # Фильтрация по региону, если указан и не равен "all"
    if region and region != 'all':
        players = players.filter(region__title=region)


    context = {'players': players}
    return render(request, template_name='players/partials/chess_player_table.html', context=context)


def add_players_to_tournament(request):

    if request.method == 'POST':
        tournament_id = request.POST.get('tournament')
        selected_players = request.POST.getlist('selected_players')

        try:
            tournament = Tournament.objects.get(id=tournament_id)
            players = ChessPlayers.objects.filter(id__in=selected_players)
            for player in players:
                tournament.players.add(player)
            tournament.save()
        except Tournament.DoesNotExist:
            pass

    return redirect('database')

