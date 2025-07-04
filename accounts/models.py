from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)