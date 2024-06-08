from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ChessPlayers, Region

from unfold.admin import ModelAdmin

from unfold.admin import ModelAdmin



admin.site.register(User)

@admin.register(ChessPlayers)
class UserAdmin(ModelAdmin):
    pass


admin.site.register(Region)



