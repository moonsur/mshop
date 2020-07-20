from django.db import models
from tastypie.resources import ModelResource
from movie.models import Movie


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['resource_uri', 'date_created', 'release_year', 'id']
