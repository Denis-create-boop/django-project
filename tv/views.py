from main import product_views as shared
from .models import Tv
from .forms import TvForm

def tv_home(request):
    return shared.listing(request, Tv)

def create_tv(request):
    return shared.edit(request, Tv, TvForm)

def product_detail(request, pk):
    return shared.detail(request, Tv, pk)

def product_update(request, pk):
    return shared.edit(request, Tv, TvForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Tv, pk)
