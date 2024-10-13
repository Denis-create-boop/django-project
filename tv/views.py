from django.shortcuts import render, redirect
from .models import Tv
from .forms import TvForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def tv_home(request):
    tv = Tv.objects.order_by('-date')
    return render(request, 'tv/tv_home.html', {'tv': tv})

class TvDetailView(DetailView):
    model = Tv
    template_name = 'tv/detail.html'
    context_object_name = 'tv'

class TvUpdateView(UpdateView):
    model = Tv
    template_name = 'tv/create.html'
    form_class = TvForm

class TvDeleteView(DeleteView):
    model = Tv
    success_url = '/tv/'
    template_name = 'tv/tv-delete.html'

def create_tv(request):
    error = ''
    if request.method == 'POST':
        form = TvForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'
    
    form = TvForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tv/create.html', data)