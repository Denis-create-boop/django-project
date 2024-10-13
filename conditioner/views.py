from django.shortcuts import render, redirect
from .models import Condition
from .forms import ConditionForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def conditioner_home(request):
    cond = Condition.objects.order_by('-date')
    return render(request, 'conditioner/conditioner_home.html', {'cond': cond})

class ConditionerDetailView(DetailView):
    model = Condition
    template_name = 'conditioner/detail.html'
    context_object_name = 'condition'

class ConditionerUpdateView(UpdateView):
    model = Condition
    template_name = 'conditioner/create.html'
    form_class = ConditionForm

class ConditionerDeleteView(DeleteView):
    model = Condition
    success_url = '/conditioner/'
    template_name = 'conditioner/condition-delete.html'


def create_condition(request):
    error = ''
    if request.method == 'POST':
        form = ConditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ConditionForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'conditioner/create.html', data)