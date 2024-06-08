from django.contrib import admin
from .models import Tournament
# Register your models here.

class ChessPlayersInline(admin.TabularInline):
    model = Tournament.players.through
    extra = 1  # Количество пустых форм для добавления новых игроков

class TournamentAdmin(admin.ModelAdmin):
    inlines = [ChessPlayersInline]
    list_display = ('title', 'start_date', 'end_date', 'gender', 'organizer', 'region')
    search_fields = ('title', 'organizer__username', 'region__title')

admin.site.register(Tournament, TournamentAdmin)