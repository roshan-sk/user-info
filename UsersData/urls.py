from django.urls import path
from .views import getUser, addUser, getOneUser, updateUser, deleteUser

urlpatterns = [
    path('get/', getUser, name='get_user'),
    path('add/', addUser, name='add_user'),
    path('<int:pk>/', getOneUser, name='get_one_user'),
    path('<int:pk>/update/', updateUser, name='update_user'),
    path('<int:pk>/delete/', deleteUser, name='delete_user'),
]