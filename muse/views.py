from django.shortcuts import render, redirect
from .models import Muse
from .forms import MuseForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def muse_home(request):
    muse = Muse.objects.order_by('-date')
    return render(request, 'muse/muse_home.html', {'muse': muse})

class MuseDetailView(DetailView):
    model = Muse
    template_name = 'muse/detail.html'
    context_object_name = 'muse'

class MuseUpdateView(UpdateView):
    model = Muse
    template_name = 'muse/create.html'
    form_class = MuseForm

class MuseDeleteView(DeleteView):
    model = Muse
    success_url = '/muse/'
    template_name = 'muse/muse-delete.html'


def create_muse(request):
    error = ''
    if request.method == 'POST':
        form = MuseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'
    
    form = MuseForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'muse/create.html', data)