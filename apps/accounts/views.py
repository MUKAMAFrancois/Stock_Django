from django.shortcuts import render,redirect
from apps.accounts.forms import (CreatingUserForm,
            Updating_User_Credintials,
            Updating_User_Profile_Form)
from apps.accounts.models import Profile
from django.contrib import messages
#from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Create your views here.

def register(request):

    if request.method=='POST':
        form=CreatingUserForm(request.POST)
        if form.is_valid():
            form.save()

            # flash message
            user=form.cleaned_data.get('username')
            messages.success(request,f'{user} was successfully registered. Login here')

            return redirect('login_user')
    else:
        form=CreatingUserForm()
    
    context={
            'form':form,
        }
    return render(request,'accounts/register.html', context )


def profile(request):
    profile=Profile.objects.all()
    context={
        'profile':profile,
    }
    return render(request,'accounts/profile.html', context)

# To Update Profile You can use ClassBAsed views or funct
#class UpdateProfile(UpdateView):
 #   model=Profile
  #  fields=['phone','adress','image']
   # template_name='accounts/update_profile.html'
   # success_url=reverse_lazy('profile')

   #N.B: remember that in template you need to include pk;; {% url 'update_profile' user.id %}


# Let's use function based Views

def updating_profile_info(request):
    
    if request.method=='POST':
        user_form=Updating_User_Credintials(request.POST, instance=request.user)
        profile_form=Updating_User_Profile_Form(request.POST,request.FILES,instance=request.user.profile) # instance is Model we need to update

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')
    
    else:
        user_form=Updating_User_Credintials(instance=request.user)
        profile_form=Updating_User_Profile_Form(instance=request.user.profile)

    dictionary={
        'user_form':user_form,
        'profile_form':profile_form
    }
    
    return render(request, 'accounts/update_profile.html',dictionary)


    