from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    client=models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    phone=models.CharField(max_length=15, default='+25078111111')
    adress=models.CharField(max_length=90, blank=True, null=True)
    image=models.ImageField(default='person.jfif', upload_to='Profile_Images')

    def __str__(self) -> str:
        return f' Profile of :{self.client.username}'