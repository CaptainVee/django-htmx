from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model

from films.forms import RegisterForm
from .models import Film
from django.views.generic.list import ListView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    template_name = 'registration/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def check_username(request):
    user = get_user_model()
    username = request.POST.get('username')
    if user.objects.filter(username = username).exists():
        return HttpResponse("<div id='username-error' class='error'> This user already exist </div>")
    else:
        return HttpResponse("<div id='username-error' class='success'> This username is available </div>")


def add_film(request):
    film_name = request.POST.get('filmname')
    film = Film.objects.create(name=film_name)
    request.user.films.add(film)
    films = request.user.films.all()
    return render(request, 'partials/film-list.html', {'films': films})


def delete_film(request, pk):
    request.user.films.remove(pk)
    films = request.user.films.all()
    return render(request, 'partials/film-list.html', {'films': films})


class FilmList(ListView):
    template_name = 'films.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        user = self.request.user
        return user.films.all()
