from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from players.forms import RegisterForm


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')



class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'players/password_reset.html'
    email_template_name = 'players/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done_page')



class CustomPasswordResetDone(PasswordResetDoneView):
    template_name = 'players/password_reset_done_page.html'


class CustomPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'players/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete_page')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'players/password_reset_complete.html'
    success_url = reverse_lazy('index')