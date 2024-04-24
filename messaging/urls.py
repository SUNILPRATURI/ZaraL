# myproject/urls.py
from django.urls import path
from .views import send_message, view_message,index,delete_message

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('', index, name='messages'),
    path('message/<int:message_id>/', view_message, name='view_message'),
    path('delete/<int:message_id>/', delete_message, name='delete_message'),
]
