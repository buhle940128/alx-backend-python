from rest_framework import viewsets, permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allows listing and retrieving conversations the authenticated user is part of.
    """
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only conversations where the current user is a participant
        return Conversation.objects.filter(participants=self.request.user)


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allows listing and retrieving messages in conversations the user is a part of.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return messages from conversations the user is involved in
        return Message.objects.filter(conversation__participants=self.request.user)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),
]
api/conversations/	POST	Create a new conversation
/api/messages/	POST	Send a message to a conversation
