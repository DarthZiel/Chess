from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['title', 'description', 'start_date', 'end_date', 'gender', 'has_age_limit', 'min_age', 'max_age', 'region']
