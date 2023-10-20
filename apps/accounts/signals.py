from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.accounts.models import Profile


#profile will be created whenever a new User is registered
@receiver(post_save, sender=User)
def create_profile(sender,instance,created,*args,**kwargs):
    if created:
        Profile.objects.create(client=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance,*args,**kwargs):
    instance.profile.save() # profile; attribute of User