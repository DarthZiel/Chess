from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
from .views import index, RegisterView, CustomPasswordResetDone, CustomPasswordResetConfirm, \
    CustomPasswordResetCompleteView

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(template_name='players/password_reset.html',
                                                      email_template_name='players/password_reset_email.html',
                                                      success_url=reverse_lazy('password_reset_done_page')),

         name='password_reset_page'),
    path('password-reset/done/', CustomPasswordResetDone.as_view(),
         name='password_reset_done_page'),
    path('password-reset/<uidb64>/<token>/',
         CustomPasswordResetConfirm.as_view(),
         name='password_reset_confirm_page'),
    path('password-reset/complete/',
         CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete_page'),

]
