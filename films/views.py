from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model

from films.forms import RegisterForm
from .models import Film
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
# Create your views here.


class IndexView(TemplateView):
    template_name = 'films/index.html'


class Login(LoginView):
    template_name = 'fimls/registration/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'films/registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


class FilmList(LoginRequiredMixin, ListView):
    template_name = 'films/films.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        user = self.request.user
        return Film.objects.filter(user=user)


def check_username(request):
    user = get_user_model()
    username = request.POST.get('username')
    if user.objects.filter(username = username).exists():
        return HttpResponse("<div id='username-error' class='error'> This user already exist </div>")
    else:
        return HttpResponse("<div id='username-error' class='success'> This username is available </div>")


@login_required
def add_film(request):
    film_name = request.POST.get('filmname')
    film = Film.objects.get_or_create(name=film_name, user=request.user)[0]
    messages.success(request, f'Successfully added {film.name}')
    films = Film.objects.filter(user=request.user)
    return render(request, 'films/partials/film-list.html', {'films': films})


@login_required
@require_http_methods(['DELETE'])
def delete_film(request, pk):
    films = Film.objects.filter(user=request.user)
    film = Film.objects.get(pk=pk).delete()
    return render(request, 'films/partials/film-list.html', {'films': films})


def search_film(request):
    search_text = request.POST.get('search_name')
    user_films = Film.objects.filter(user=request.user)
    results = Film.objects.filter(name__icontains=search_text).exclude(
        name__in=user_films.values_list('name', flat=True))
    context = {'results': results}
    return render(request, 'films/partials/search-results.html', context)


def clear(request):
    return HttpResponse("")


@login_required
def film_details(request, pk):
    film = Film.objects.get(pk=pk)
    context = {"film": film}
    return render(request, 'films/film_details.html', context)


@login_required
def upload_photo(request, pk):
    film = Film.objects.get(pk=pk)
    image = request.FILES.get('photo')
    film.photo.save(image.name, image)
    context = {"film": film}
    return render(request, 'films/partials/detail_img.html', context)
