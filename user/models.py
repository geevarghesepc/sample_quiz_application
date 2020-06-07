from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
import jwt
from django.conf import settings


class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = 'user'

    @property
    def token(self):
        return self._generate_token()

    def _generate_token(self):
        dt = datetime.now() + timedelta(minutes=120)
        token = jwt.encode({'id':self.pk, 'exp': dt}, settings.SECRET_KEY).decode('utf8')

        return token
