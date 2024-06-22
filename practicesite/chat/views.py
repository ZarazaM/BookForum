from django.db.models import Subquery
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Chat, Message
from .forms import ChatCreationForm
from users.models import Profile


def allChats(request):
    chat_list = Chat.objects.all()
    form = ChatCreationForm()

    context = {
        'chat_list': chat_list,
        'form': form,
    }
    return render(request, 'chat/index.html', context=context)


def specificChat(request, chat_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    queryset = Message.objects.filter(chat__exact=chat_id)
    chat_messages = queryset
    user = request.user
    return render(request, 'chat/specific.html', context={'chat': chat, 'messages': chat_messages, 'user': user})


def send(request):
    text = request.POST['message']
    user_id = request.POST['user_id']
    chat_id = request.POST['chat_id']
    # author = User.objects.filter(pk=user_id)
    author = get_object_or_404(User, pk=user_id)
    # chat = Chat.objects.filter(pk=chat_id)
    chat = get_object_or_404(Chat, pk=chat_id)
    new_message = Message.objects.create(text=text, author=author, chat=chat, pub_time=timezone.now())
    new_message.save()
    return HttpResponse('Message sent successfully')
    # return redirect('begin')


def getMessages(request, chat_id):
    chat_details = Chat.objects.get(pk=chat_id)
    messages = Message.objects.filter(chat=chat_details.id).order_by('pub_time')
    authors = User.objects.filter(id__in=Subquery(messages.values('author_id')))
    profiles = Profile.objects.filter(user__in=Subquery(messages.values('author_id')))
    return JsonResponse({"messages":list(messages.values()), "authors":list(authors.values()), "profiles":list(profiles.values())})


def createChat(request):
    chat_name = request.POST['name']
    new_chat = Chat.objects.create(name=chat_name, creator=request.user, create_time=timezone.now())
    new_chat.save()
    chat_id = new_chat.id
    return redirect('specific', chat_id)
