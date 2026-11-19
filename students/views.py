from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import StudentForm
from .models import Student

from django.db.models import Q
from django.core.paginator import Paginator

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
    query = request.GET.get('q', '')
    selected_course = request.GET.get('course', '')
    students = Student.objects.filter(trainer=request.user)

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(student_id__icontains=query) |
            Q(email__icontains=query)
        )
    if selected_course:
        students = students.filter(course=selected_course)
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'students': page_obj,
        'page_obj': page_obj,
        'query': query,
        'selected_course': selected_course,
        'course_choices': Student.COURSE_CHOICES,
    }

    return render(request, 'students/student_list.html', context)

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


