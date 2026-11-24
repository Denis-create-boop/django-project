from main import product_views as shared
from .models import Phone
from .forms import PhoneForm

def phone_home(request):
    return shared.listing(request, Phone)

def create_phone(request):
    return shared.edit(request, Phone, PhoneForm)

def product_detail(request, pk):
    return shared.detail(request, Phone, pk)

def product_update(request, pk):
    return shared.edit(request, Phone, PhoneForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Phone, pk)
