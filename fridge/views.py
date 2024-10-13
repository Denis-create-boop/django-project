from django.shortcuts import render, redirect
from .models import Fridge
from .forms import FridgeForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def fridge_home(request):
    fridge = Fridge.objects.order_by('-date')
    return render(request, 'fridge/fridge_home.html', {'fridge': fridge})

class FridgeDetailView(DetailView):
    model = Fridge
    template_name = 'fridge/detail.html'
    context_object_name = 'fridge'

class FridgeUpdateView(UpdateView):
    model = Fridge
    template_name = 'fridge/create.html'
    form_class = FridgeForm

class FridgeDeleteView(DeleteView):
    model = Fridge
    success_url = '/fridge/'
    template_name = 'fridge/fridge-delete.html'

def create_fridge(request):
    error = ''
    if request.method == 'POST':
        form = FridgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'
    
    form = FridgeForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'fridge/create.html', data)
     