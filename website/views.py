from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    # check to see if customer is logged in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        #Authenticate User
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again.Thanks!")
            return redirect('home')

    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate user and log them In
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = 'username', password = 'password')
            login(request, user)
            messages.success(request, "You Have Been Succesfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})
