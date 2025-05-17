from django.db.models import *
from django.contrib.auth.models import User

# Create your models here.
class Event(Model):
    EVENT_TYPES = [
        ('exam', 'Exam'),
        ('test', 'Test'),
        ('school_event', 'School Event'),
        ('parent_meeting', 'Parent Meeting'),
        ('personal_event', 'Personal Event'),
    ]
    title = CharField(max_length=255, verbose_name='назва')
    event_type = CharField(max_length=20, choices=EVENT_TYPES, verbose_name='тип')
    start_time = DateTimeField(verbose_name='початок')
    duration = IntegerField(verbose_name='тривалість')
    content = TextField(null=True, blank=True, verbose_name='опис')
    location = CharField(max_length=255, null=True, blank=True, verbose_name='місце')
    created_by = ForeignKey(User, on_delete=CASCADE, verbose_name='автор')

    class Meta:
        verbose_name='подія'
        verbose_name_plural='події'

    def __str__(self):
        return self.title

class EventParticipant(Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('pending', 'Pending'),
    ]
    event = ForeignKey(Event, on_delete=CASCADE, verbose_name='подія')
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='учасник')
    status = CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='статус')

    class Meta:
        verbose_name='учасник події'
        verbose_name_plural='учасники події'

    def __str__(self):
        return self.user.username

class Task(Model):
    title = CharField(max_length=255, verbose_name='назва')
    due_date = DateField(verbose_name="термін")
    content = TextField(null=True, blank=True, verbose_name='опис')
    event = ForeignKey(Event, on_delete=SET_NULL, null=True, blank=True, verbose_name='подія')
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='автор')
    status = CharField(max_length=10, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', verbose_name='Статус')

    class Meta:
        verbose_name='задача'
        verbose_name_plural='задачі'

    def __str__(self):
        return self.title

class Comment(Model):
    event = ForeignKey(Event, on_delete=CASCADE, verbose_name='подія')
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='автор')
    comment = TextField(verbose_name='коментар')
    created_at = DateTimeField(auto_now_add=True, verbose_name='дата')

    class Meta:
        verbose_name='коментар'
        verbose_name_plural='коментарі'

class Notification(Model):
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='автор')
    message = TextField(verbose_name='повідомлення')
    is_read = BooleanField(default=False, verbose_name='прочитане?')
    created_at = DateTimeField(auto_now_add=True, verbose_name='дата')

    class Meta:
        verbose_name='повідомлення'
        verbose_name_plural='повідомлення'


class File(Model):
    event = ForeignKey(Event, on_delete=CASCADE, verbose_name='подія')
    file_path = FileField(upload_to='event_files/', verbose_name='розташування')
    uploaded_at = DateTimeField(auto_now_add=True, verbose_name='дата завантаження')

    class Meta:
        verbose_name='файл'
        verbose_name_plural='файли'
