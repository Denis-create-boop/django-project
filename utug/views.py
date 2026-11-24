from main import product_views as shared
from .models import Utug
from .forms import UtugForm

def utug_home(request):
    return shared.listing(request, Utug)

def create_utug(request):
    return shared.edit(request, Utug, UtugForm)

def product_detail(request, pk):
    return shared.detail(request, Utug, pk)

def product_update(request, pk):
    return shared.edit(request, Utug, UtugForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Utug, pk)
