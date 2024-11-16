from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_form/', views.contact_form, name='contact'),
    path('success/', views.success, name='success'),
#     path('task/update/<int:pk>/', views.task_update,
#          name='task_update'),
 ]

# after defining the app routes
# we take these urlpatterns and register them to the project