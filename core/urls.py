from django.urls import path, re_path
from django.utils import archive

from . import views
from .views import index, categories, about

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('cats/<int:catid>/', views.categories, name="categories"),
    path("archive/2003/", views.archive),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name="archive"),
]

