from django.urls import path
from . import views

urlpatterns = [
    path('<str:model_name>/', views.list_objects),
    path('<str:model_name>/<int:pk>/', views.list_object_byID),
    path('<str:model_name>/create/', views.create_object),
    path('<str:model_name>/update/<int:pk>/', views.update_object),
    path('<str:model_name>/delete/<int:pk>/', views.delete_object),
]
