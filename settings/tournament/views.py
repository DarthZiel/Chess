from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tournament
from players.models import Region


# Create your views here.
class TournamentList(ListView):
    template_name = 'tournament/tournaments.html'
    model = Tournament
    context_object_name = 'tournaments'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direction_asc'] = self.request.GET.get('direction')
        context['regions'] = Region.objects.all()
        return context


    def get_queryset(self):
        queryset = Tournament.objects.all()
        sort_by = self.request.GET.get('sort_by', 'title')
        direction = self.request.GET.get('direction', 'asc')

        if direction =='desc':
            sort_by = '-' + sort_by

        return queryset.order_by(sort_by)


from datetime import date

def search(request):
    name = request.GET.get('name')  # Поле для поиска (fide_id или last_name)
    status = request.GET.get('status')  # Строка поиска
    region = request.GET.get('region')


    match status:
        case "all":
            tournaments = Tournament.objects.all()
        case "planned":
            tournaments = Tournament.objects.filter(start_date__lte=date.today(), end_date__lte=date.today())
        case "in_progress":
            tournaments = Tournament.objects.filter(start_date__gte=date.today(), end_date__lte=date.today())
        case "completed":
            tournaments = Tournament.object.filter(end_date__lte=date.today())

    # Фильтрация по полю поиска и строке поиска
    if name:
        tournaments = tournaments.filter(title__icontains=name)

    # Фильтрация по региону, если указан и не равен "all"
    if region and region != 'all':
        tournaments = tournaments.filter(region__title=region)


    context = {'tournaments': tournaments}
    return render(request, template_name='tournament/partials/tournaments_table.html', context=context)

class TournamentDetailView(DetailView):
    model = Tournament
    context_object_name = 'tournament'






