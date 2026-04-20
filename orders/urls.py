from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('order/<int:pk>/notes/create/', views.order_note_create, name='order_note_create'),
    path('edit/<int:pk>/', views.order_update, name='order_update'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),
]