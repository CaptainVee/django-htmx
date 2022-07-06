from django.shortcuts import render, redirect
import random
from .models import Article
from .forms import ArticleForm

# Create your views here.


def article_create_view(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ArticleForm()

    return render(request, 'articles/create.html', {'form': form})

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)


def article_search_view(request):

    query = request.GET.get("q")

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)


def home_view(request, *args, **kwargs):
    # article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "articles": article_queryset,
    }
    return render(request, "articles/home.html", context=context)
