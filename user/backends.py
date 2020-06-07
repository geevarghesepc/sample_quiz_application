import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import User


class JWTAuth(authentication.BaseAuthentication):
    auth_prefix = "bearer"

    def authenticate(self, request):

        header = self.authenticate_header(request).split()
        if not header:
            return None

        if self.auth_prefix != header[0].decode('utf8').lower():
            return None

        token = header[1].decode('utf8')

        if not token:
            return None

        return self.auth_creds(request, token)


    def auth_creds(self, request, token):

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = "Failed to decrypt token"
            print(msg)
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = "User not found"
            print(msg)
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
