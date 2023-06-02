from django.urls import path
from .views import *

app_name="chat"

urlpatterns = [
    path('messages/', messages, name='messages'),
    path('messages/<int:receiver_id>/', messages, name='messages'),
]