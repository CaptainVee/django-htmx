from django.shortcuts import render
from .models import Course, Module
# Create your views here.


def courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}

    return render(request, 'university/home.html', context)


def modules(request):
    course = request.GET.get('course')
    '''
    request can get the course pk because of the 'name=course' variable that was passed
    in the select field in the home.html file, you probably could use hx-post instead of
    get, i really don't know '''

    modules = Module.objects.filter(course=course)
    context = {"modules": modules}

    return render(request, 'university/partials/modules.html', context)
