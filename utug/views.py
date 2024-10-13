from django.shortcuts import render, redirect
from .models import Utug
from .forms import UtugForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def utug_home(request):
    utug = Utug.objects.order_by('-date')
    return render(request, 'utug/utug_home.html', {'utug': utug})

class UtugDetailView(DetailView):
    model = Utug
    template_name = 'utug/detail.html'
    context_object_name = 'utug'

class UtugUpdateView(UpdateView):
    model = Utug
    template_name = 'utug/create.html'
    form_class = UtugForm

class UtugDeleteView(DeleteView):
    model = Utug
    success_url = '/utug/'
    template_name = 'utug/utug-delete.html'

def create_utug(request):
    error = ''
    if request.method == 'POST':
        form = UtugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'
    
    form = UtugForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'utug/create.html', data)