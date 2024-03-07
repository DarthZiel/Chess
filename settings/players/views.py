from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import RegisterForm


@login_required
def index(request):
    return render(request, 'players/index.html')


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
