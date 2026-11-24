from main import product_views as shared
from .models import Condition
from .forms import ConditionForm

def conditioner_home(request):
    return shared.listing(request, Condition)

def create_condition(request):
    return shared.edit(request, Condition, ConditionForm)

def product_detail(request, pk):
    return shared.detail(request, Condition, pk)

def product_update(request, pk):
    return shared.edit(request, Condition, ConditionForm, pk)

def product_delete(request, pk):
    return shared.remove(request, Condition, pk)
