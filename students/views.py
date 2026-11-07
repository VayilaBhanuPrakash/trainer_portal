from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import StudentForm
from .models import Student

@login_required
def create_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.trainer = request.user
            student.save()

            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/create_student.html', {'form': form})

@login_required
def student_list_view(request):
    students = Student.objects.filter(trainer=request.user)

    return render(request, 'students/student_list.html', {'students': students})

@login_required
def update_student_view(request,student_id):
    student = get_object_or_404(Student, student_id=student_id, trainer=request.user)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/update_student.html', {'form': form, 'student': student})


@login_required
def delete_student_view(request, student_id):
    student = get_object_or_404(Student, student_id=student_id, trainer=request.user)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/delete_student.html', {'student': student})


