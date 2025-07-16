from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='task')

urlpatterns = [
    path("", views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('task/<int:pk>', views.individual_task, name='task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),

    # DRF APIs
    path('api/register/', views.RegisterAPI.as_view(), name='api-register'),
    path('api/login/', views.LoginAPI.as_view(), name='api-login'),
]

urlpatterns += router.urls  




'''
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('task/<int:pk>', views.individual_task, name='task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),




     # DRF APIs
    path('api/register/', views.RegisterAPI.as_view(), name='api-register'),
    path('api/login/', views.LoginAPI.as_view(), name='api-login'),

]
'''
