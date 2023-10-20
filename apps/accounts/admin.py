from django.contrib import admin
from apps.accounts.models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display=['client','phone','adress']