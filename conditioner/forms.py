from main.product_forms import ProductForm
from .models import Condition
class ConditionForm(ProductForm):
    class Meta:
        model = Condition
        fields = ['title','model','full_text','date','price','discount']
