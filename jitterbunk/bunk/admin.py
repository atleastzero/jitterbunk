from django.contrib import admin

from .models import UserProfile, Bunk

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'photo_url']
    readonly_field=['slug']

@admin.register(Bunk)
class BunkAdmin(admin.ModelAdmin):
    fields = ['from_user', 'to_user']
    readonly_field=['time_sent']
