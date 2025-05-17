from django.contrib import admin
from .models import Task, Event, EventParticipant, Comment, Notification, File

# Register your models here.
# admin.site.register(Task)
# admin.site.register(Event)
# admin.site.register(EventParticipant)
# admin.site.register(Comment)
# admin.site.register(Notification)
# admin.site.register(File)

class TaskAdmin(admin.ModelAdmin):
    # Список полів, які мають відображатися в адмінці
    list_display = ('title', 'due_date', 'user', 'status')
    # Список полів, за якими можна фільтрувати
    list_filter = ('due_date', 'status', 'user')
    # Кількість записів на сторінку
    list_per_page = 20

    # Групи полів у картці задачі
    fieldsets = (
        ('Task info', {
            'fields': ('title', 'content')
        }),
        ('Parameters', {
            'fields': ('due_date', 'event', 'user', 'status')
        }),
    )

    def has_module_permission(self, request):
        return not request.user.groups.filter(name='Викладач').exists()


admin.site.register(Task, TaskAdmin)

class EventAdmin(admin.ModelAdmin):
    # Список полів, які мають відображатися в адмінці
    list_display = ('title', 'event_type', 'start_time', 'created_by', 'location')
    # Список полів, за якими можна фільтрувати
    list_filter = ('start_time', 'created_by', 'event_type')
    # Кількість записів на сторінку
    list_per_page = 20

    # Групи полів у картці задачі
    fieldsets = (
        ('Event info', {
            'fields': ('title', 'content')
        }),
        ('Event time', {
            'fields': ('start_time', 'duration')
        }),
        ('Parameters', {
            'fields': ('event_type', 'location', 'created_by')
        }),
    )

    def has_module_permission(self, request):
        return not request.user.groups.filter(name='Викладач').exists()

admin.site.register(Event, EventAdmin)


class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'status')
    list_filter = ('event', 'user', 'status')
    # Кількість записів на сторінку
    list_per_page = 20

admin.site.register(EventParticipant, EventParticipantAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'created_at')
    list_filter = ('event', 'user', 'created_at')
    # Кількість записів на сторінку
    list_per_page = 20

    # Групи полів у картці задачі
    fieldsets = (
        ('Comment info', {
            'fields': ('event', 'comment')
        }),
        ('Parameters', {
            'fields': ('user', 'created_at')
        }),
    )

    def has_module_permission(self, request):
        return not request.user.groups.filter(name='Викладач').exists()

admin.site.register(Comment, CommentAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_read')
    list_filter = ('user', 'created_at', 'is_read')
    # Кількість записів на сторінку
    list_per_page = 20

    # Групи полів у картці коментаря
    fieldsets = (
        ('Comment info', {
            'fields': ('user', 'message')
        }),
        ('Parameters', {
            'fields': ('is_read', 'created_at')
        }),
    )

    def has_module_permission(self, request):
        return not request.user.groups.filter(name='Викладач').exists()

admin.site.register(Notification, NotificationAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ('event', 'file_path', 'uploaded_at')
    list_filter = ('event', 'file_path', 'uploaded_at')
    # Кількість записів на сторінку
    list_per_page = 20

    # Групи полів у картці файлу
    fieldsets = (
        ('File info', {
            'fields': ('event', 'file_path')
        }),
        ('Parameters', {
            'fields': ('uploaded_at',)
        }),
    )

    def has_module_permission(self, request):
        return not request.user.groups.filter(name='Викладач').exists()

admin.site.register(File, FileAdmin)
