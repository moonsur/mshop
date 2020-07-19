from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([movie.name for movie in movies])
    # return HttpResponse(output)
    return render(request, 'movie/index.html', {'movies': movies})


def detail(request, mov_id):
    movie = get_object_or_404(Movie, id=mov_id)
    return render(request, 'movie/detail.html', {'movie': movie})
