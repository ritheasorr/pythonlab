from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm


# Create your views here.
def loginView(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print("Username", user)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login/login.html', {'page': page})


def registerView(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('index')

    context = {'form': form, 'page': page}
    return render(request, 'login/login.html', context)


@login_required(login_url='login')
def index(request):
    return render(request, 'pages/index.html')
