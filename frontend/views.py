from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Event, Task, EventParticipant
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.utils.dateparse import parse_datetime


# Create your views here.

def is_not_parent(user):
    return not user.groups.filter(name='Батьки').exists()


def index(request):
    return render(request, 'index.html')


def calendar(request):
    events = Event.objects.all()
    if request.user.groups.filter(name='Студент').exists():
        student_group = Group.objects.get(name='Студент')
        users = User.objects.filter(groups=student_group)
    else:
        users = User.objects.all()
    return render(request, 'calendar.html', {'events': events, 'users': users})


def tasks(request):
    tasks_list = Task.objects.all()
    events = Event.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks_list, 'events': events})


@login_required(login_url='/login/')
@user_passes_test(is_not_parent)
def add_task(request):
    if request.method == 'POST' and request.user.groups.filter(name='Батьки').exists():
        return HttpResponseForbidden("Батькам заборонено додавати записи.")

    if request.user.groups.filter(name='Студент').exists():
        return HttpResponseForbidden("Студентам заборонено створювати завдання.")

    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        content = request.POST.get('content')
        event_id = request.POST.get('event_id')
        status = request.POST.get('status')

        # Перевірка, чи є вибрана подія
        event = Event.objects.get(id=event_id) if event_id else None

        # Створення нового завдання
        new_task = Task(
            title=title,
            due_date=due_date,
            content=content,
            event=event,
            user=request.user,
            status=status
        )
        new_task.save()

        # Перенаправлення користувача після успішного додавання
        return redirect('tasks')  # Можна змінити на будь-який URL для перенаправлення

    return HttpResponse(status=405)  # Якщо метод не POST, повертаємо помилку


@login_required(login_url='/login/')
@user_passes_test(is_not_parent)
def add_event(request):
    if request.method == 'POST':
        if request.user.groups.filter(name='Батьки').exists():
            return HttpResponseForbidden("Батькам заборонено додавати події.")

        title = request.POST['title']
        event_type = request.POST['event_type']
        start_time = request.POST['start_time']
        duration = request.POST['duration']
        content = request.POST.get('content', '')
        location = request.POST.get('location', '')
        participants_ids = request.POST.getlist('participants')

        if request.user.groups.filter(name='Студент').exists():
            # Перевірка: всі обрані учасники повинні бути зі студентської групи
            student_group = Group.objects.get(name='Студент')
            allowed_ids = User.objects.filter(groups=student_group).values_list('id', flat=True)
            for pid in participants_ids:
                if int(pid) not in allowed_ids:
                    return HttpResponseForbidden("Студенти можуть запрошувати лише інших студентів.")

        event = Event.objects.create(
            title=title,
            event_type=event_type,
            start_time=start_time,
            duration=duration,
            content=content,
            location=location,
            created_by=request.user  # якщо така є
        )

        for user_id in participants_ids:
            user = User.objects.get(pk=user_id)
            EventParticipant.objects.create(event=event, user=user)
        # Перенаправлення користувача на сторінку подій або на деталі події
        return redirect('calendar')  # Наприклад, перенаправлення на список подій (або на конкретну подію)

    return HttpResponse(status=405)


def profile(request):
    return render(request, 'profile.html')


@require_POST
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.status == 'completed':
        task.status = 'pending'
    else:
        task.status = 'completed'
    task.save()
    return JsonResponse({
        'success': True,
        'new_status': task.status
    })
