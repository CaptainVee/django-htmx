from django.shortcuts import render, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.http import QueryDict
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    students = Student.objects.all()
    paginator = Paginator(students, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    if request.htmx:
        return render(request, 'student/partials/list.html', context)
    return render(request, 'student/index.html', context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {"student": student}
    if request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = StudentForm(data, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'student/partials/student-details.html', context)

        return render(request, 'student/partials/student-edit-form.html', context)

    return render(request, 'student/student.html', context)


def student_edit_form(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    context = {
        "student": student,
        "form": form
    }
    return render(request, 'student/partials/student-edit-form.html', context)
