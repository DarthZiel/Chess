from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ChessPlayers

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'phone', 'full_name')


class ChessPlayerForm(forms.ModelForm):

    class Meta:
        model = ChessPlayers
        fields = ['fide_id', 'last_name', 'first_name', 'region']