from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from student.models import Student
from student.forms import StudentForm

def index(request):
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)

