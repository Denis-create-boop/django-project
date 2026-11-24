from main import product_views as shared
from .models import Muse
from .forms import MuseForm

def muse_home(request):
    return shared.listing(request, Muse)

def create_muse(request):
    return shared.edit(request, Muse, MuseForm)

def product_detail(request, pk):
    return shared.detail(request, Muse, pk)

def product_update(request, pk):
    return shared.edit(request, Muse, MuseForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Muse, pk)
