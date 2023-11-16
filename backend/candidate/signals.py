from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import Candidate,Education,Referee


@receiver(pre_save, sender=Candidate)
def create_user_for_candidate(sender, instance, *args, **kwargs):
    if instance.id is None:
        email = instance._email
        password = instance._password

        user = CustomUser(email=email)
        user.set_password(password)
        user.save()

        instance.user = user