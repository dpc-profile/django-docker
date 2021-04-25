from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URLs)
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render (request, template_name, context)

'''
def register(request):

    registered = False

    if(request.method == 'POST'):
        userForm = forms.UserForm(data=request.POST)
        profileForm = forms.UserProfileInfoForm(data=request.POST)

        if((userForm.is_valid()) and (profileForm.id_valid())):
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            if('profileImage' in request.FILES):
                profile.profileImage = request.FILES['profileImage']

            profile.save()

            registered = True
        else:
            print(userForm.errors, profileForm.errors)   
    else:
        userForm = forms.UserForm()
        profileForm = forms.UserProfileInfoForm()

    return render(request, 'basic/registration.html', {'userForm':userForm, 'profileForm':profileForm, 'registered':registered})
'''