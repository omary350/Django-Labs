from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
# def login (request):
#     return render(request, 'login/login.html')


def login(request):
    dataform = LoginForm()
    if request.method == 'POST':
        dataform = LoginForm(request.POST)
        if dataform.is_valid():
            dataform.save()
            return redirect('/login')
    
    return render(request, 'login/login.html', {'form': dataform})