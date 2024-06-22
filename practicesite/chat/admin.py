from django.contrib import admin
from .models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    fields = ['name', 'creator', 'create_time']

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Publication info', {'fields': ['chat', 'pub_time', 'author']}),
    ]
    list_filter = ['pub_time']
    search_fields = ['text']


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
