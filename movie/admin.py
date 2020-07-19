from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'genre', 'reveiw')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
