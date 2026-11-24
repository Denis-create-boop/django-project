from django.shortcuts import render
from .permissions import manager_required

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

@manager_required
def add(request):
    return render(request, 'main/add.html')

@manager_required
def dashboard(request):
    return render(request, 'main/dashboard.html')
