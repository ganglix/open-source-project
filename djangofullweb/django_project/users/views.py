from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm # a class inherit from UserCreationForm

# Create your views here.
def register(request):
    # already existing class to be converted to html
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save/create the user to database automatically by django
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can log in now!')
            return redirect('login')
    else:
        form =  UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')