from main.product_forms import ProductForm
from .models import Wash
class WashForm(ProductForm):
    class Meta:
        model = Wash
        fields = ['title','model','full_text','date','price','discount']
