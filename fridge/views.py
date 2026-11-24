from main import product_views as shared
from .models import Fridge
from .forms import FridgeForm

def fridge_home(request):
    return shared.listing(request, Fridge)

def create_fridge(request):
    return shared.edit(request, Fridge, FridgeForm)

def product_detail(request, pk):
    return shared.detail(request, Fridge, pk)

def product_update(request, pk):
    return shared.edit(request, Fridge, FridgeForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Fridge, pk)
