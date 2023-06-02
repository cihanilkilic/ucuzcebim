from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q

from PIL import Image
import os


@login_required(login_url="user:Login")
def messages(request, receiver_id=None):
    conversations = None
    receiver = None

    if receiver_id:
        receiver = User.objects.get(id=receiver_id)
        conversations = Message.objects.filter(sender=request.user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=request.user)
        conversations = conversations.order_by('timestamp')

    if request.method == 'POST':
        receiver_id = request.POST.get('receiver')
        receiver = User.objects.get(id=receiver_id)
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if image and not content:
            message = Message(sender=request.user, receiver=receiver, image=image)
            message.save()
        elif content and not image:
            message = Message(sender=request.user, receiver=receiver, content=content)
            message.save()
        elif content and image:
            message = Message(sender=request.user, receiver=receiver, content=content, image=image)
            message.save()

        return redirect('chat:messages', receiver_id=receiver_id)

    users = User.objects.exclude(id=request.user.id).filter(
        Q(sent_messages__receiver=request.user) | Q(received_messages__sender=request.user)
    ).distinct()
    users_with_full_names = []
    for user in users:
        full_name = user.first_name + " " + user.last_name
        users_with_full_names.append((user, full_name))

    return render(request, 'chat/messages.html', {'users': users, 'conversations': conversations, 'receiver': receiver,'users': users_with_full_names})
