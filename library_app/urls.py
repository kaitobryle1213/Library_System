# library_app/urls.py

from django.urls import path
from .views import user_list, home, add_user

urlpatterns = [
    path('', home, name='home'),
    path('users/', user_list, name='user_list'),
    path('add_user/', add_user, name='add_user'),
]
