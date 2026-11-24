from main import product_views as shared
from .models import Computer
from .forms import ComputerForm

def comp_home(request):
    return shared.listing(request, Computer)

def create_computer(request):
    return shared.edit(request, Computer, ComputerForm)

def product_detail(request, pk):
    return shared.detail(request, Computer, pk)

def product_update(request, pk):
    return shared.edit(request, Computer, ComputerForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Computer, pk)
