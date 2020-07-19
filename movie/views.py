from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([movie.name for movie in movies])
    # return HttpResponse(output)
    return render(request, 'movie/index.html', {'movies': movies})
