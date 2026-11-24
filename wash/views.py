from main import product_views as shared
from .models import Wash
from .forms import WashForm

def wash_home(request):
    return shared.listing(request, Wash)

def create_wash(request):
    return shared.edit(request, Wash, WashForm)

def product_detail(request, pk):
    return shared.detail(request, Wash, pk)

def product_update(request, pk):
    return shared.edit(request, Wash, WashForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Wash, pk)
