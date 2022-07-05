from django.shortcuts import render
import random
from .models import Article

# Create your views here.


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Justin"  # hard coded
    random_id = random.randint(1, 4)  # pseudo random

    # from the database??
    # article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object": article_queryset,
    }
    return render(request, "articles/home.html", context=context)
