from django.shortcuts import render, redirect
from .models import Wash
from .forms import WashForm
from django.views.generic import DetailView, DeleteView, UpdateView

# Create your views here.
def wash_home(request):
    wash = Wash.objects.order_by('-date')
    return render(request, 'wash/wash_home.html', {'wash': wash})

class WashDetailView(DetailView):
    model = Wash
    template_name = 'wash/detail.html'
    context_object_name = 'wash'

class WashUpdateView(UpdateView):
    model = Wash
    template_name = 'wash/create.html'
    form_class = WashForm

class WashDeleteView(DeleteView):
    model = Wash
    success_url = '/wash/'
    template_name = 'wash/wash-delete.html'

def create_wash(request):
    error = ''
    if request.method == 'POST':
        form = WashForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'
    
    form = WashForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'wash/create.html', data)