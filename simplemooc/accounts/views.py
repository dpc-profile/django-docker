from django.shortcuts import render

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
