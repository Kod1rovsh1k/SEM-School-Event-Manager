"""
URL configuration for SEM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views as frontend_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend_views.index, name='index'),
    path('calendar/', frontend_views.calendar, name='calendar'),
    path('tasks/', frontend_views.tasks, name='tasks'),
    path('profile/', frontend_views.profile, name='profile'),
    path('add_task/', frontend_views.add_task, name='add_task'),
    path('add_event/', frontend_views.add_event, name='add_event'),
    path('tasks/toggle-status/<int:task_id>/', frontend_views.toggle_task_status, name='toggle_task_status'),
    path('login/', users_views.UserLoginView.as_view(), name='login'),
    path('logout/', users_views.UserLogoutView.as_view(), name='logout'),
    path('register/', users_views.UserRegisterView.as_view(), name='register'),
    path('user_profile/', users_views.UserProfileView.as_view(), name='user_profile'),
]
