from django.contrib import admin
from .models import Schedule, Episode, Show


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    pass
