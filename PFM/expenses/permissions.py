from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions    
from .models import Profile

class TelegramAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        chat_id = request.META.get('HTTP_X_CHAT_ID')
        print(chat_id)
        if not chat_id:
            return None

        try:
            profile = Profile.objects.get(chat_id=chat_id)
            user = User.objects.get(profile=profile)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)