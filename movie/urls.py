from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mov_id>', views.detail, name='detail')
]
