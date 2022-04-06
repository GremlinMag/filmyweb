from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, DodatkoweInfo, Ocena, Aktor
from .forms import FilmForm, DodatkoweInfoForm , OcenaForm, AktorForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# Create your views here.
def filmy(request):
    # return HttpResponse("<h1>To test</h1>")
    filmy = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': filmy})

@login_required
def nowy_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)
    form_ocena = OcenaForm(request.POST or None)
    form_aktor = AktorForm(request.POST or None)

    if form_film.is_valid() and form_dodatkowe.is_valid():
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(filmy)

    filmy = Film.objects.all()
    return render(request, 'film_form.html', {'filmy': filmy,
                                              'form': form_film,
                                              'form_dodatkowe': form_dodatkowe,
                                              'form_ocena': form_ocena,
                                              'form_aktor': form_aktor,
                                              'nowy': True})

@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)

    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    form_ocena = OcenaForm(request.POST or None)
    form_aktor = AktorForm(request.POST or None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.save()

    if request.method == 'POST':
        if 'imie' in request.POST:
            form_aktor.save()

    if form_film.is_valid() and form_dodatkowe.is_valid():
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(filmy)

    filmy = Film.objects.all()
    return render(request, 'film_form.html', {'filmy': filmy,
                                              'form': form_film,
                                              'form_dodatkowe': form_dodatkowe,
                                              'form_ocena': form_ocena,
                                              'form_aktor': form_aktor,
                                              'nowy': False})

@login_required
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(filmy)

    filmy = Film.objects.all()
    return render(request, 'confirm.html', {'filmy': filmy,
                                              'film': film})

def show_film(request, id):
    film = get_object_or_404(Film, pk=id)
    oceny = Ocena.objects.filter(film=film)
    aktorzy = film.aktorzy.all()

    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    filmy = Film.objects.all()
    return render(request, 'film_show.html', {'film': film,
                                              'oceny': oceny,
                                              'aktorzy': aktorzy,
                                              'filmy': filmy,})

def about_me(request):
    filmy = Film.objects.all()
    return render(request, 'about_me.html', {'filmy': filmy,})