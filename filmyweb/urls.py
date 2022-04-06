from django.urls import path
from .views import filmy, nowy_film, edytuj_film, usun_film, show_film, about_me

urlpatterns = [
    path('', filmy, name="filmy"),
    #path('all/', filmy, name="filmy"),
    path('nowy/', nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/', usun_film, name="usun_film"),
    path('show/<int:id>/', show_film, name="show_film"),
    path('about_me/', about_me, name="about_me"),
]