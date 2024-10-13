from django.shortcuts import render, redirect
from .models import Computer
from .forms import ComputerForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def comp_home(request):
    comp = Computer.objects.order_by('-date')
    return render(request, 'computer/comp_home.html', {'comp': comp})

class ComputerDetailView(DetailView):
    model = Computer
    template_name = 'computer/detail.html'
    context_object_name = 'comp'

class ComputerUpdateView(UpdateView):
    model = Computer
    template_name = 'computer/create.html'
    form_class = ComputerForm

class ComputerDeleteView(DeleteView):
    model = Computer
    success_url = '/computer/'
    template_name = 'computer/comp-delete.html'

def create_computer(request):
    error = ''
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ComputerForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'computer/create.html', data)