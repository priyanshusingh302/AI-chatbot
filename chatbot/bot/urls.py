# urls.py in your app

from django.urls import path
from .views import remove_spaces

urlpatterns = [
    path('api/chat/', remove_spaces, name='remove_spaces'),
]
