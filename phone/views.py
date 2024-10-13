from django.shortcuts import render, redirect
from .models import Phone
from .forms import PhoneForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def phone_home(request):
    phone = Phone.objects.order_by('-date')
    return render(request, 'phone/phone_home.html', {'phone': phone})

class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'phone/detail.html'
    context_object_name = 'phone'

class PhoneUpdateView(UpdateView):
    model = Phone
    template_name = 'phone/create.html'
    form_class = PhoneForm

class PhoneDeleteView(DeleteView):
    model = Phone
    success_url = '/phone/'
    template_name = 'phone/phone-delete.html'

def create_phone(request):
    error = ''
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'
    
    form = PhoneForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'phone/create.html', data)