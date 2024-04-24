# myapp/views.py
from django.shortcuts import render, redirect
from core.models import CustomUser

from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

from cryptography.fernet import Fernet

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sender = request.user
            receiver_username = form.cleaned_data['receiver']
            content = form.cleaned_data['content']
            print('form_valid')

            # Check if receiver exists
            if CustomUser.objects.filter(username=receiver_username).exists():

                message = Message(sender=sender, receiver=receiver_username, content=content)
                message.save()

                return redirect('messages')
            else:
                return render(request,'core/404.html')
            


    else:
        form = MessageForm()
    return render(request, 'messages/send.html', {'sendMessage': form})

@login_required
def view_message(request, message_id):
    message = Message.objects.get(pk=message_id)

    
    return render(request, 'messages/index.html', {'message': message})
@login_required
def delete_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.delete()
    return redirect('messages')
@login_required
def index(request):
    messages = Message.objects.all()
    return render(request, 'messages/index.html', {'messages': messages})