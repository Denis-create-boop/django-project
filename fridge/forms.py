from main.product_forms import ProductForm
from .models import Fridge
class FridgeForm(ProductForm):
    class Meta:
        model = Fridge
        fields = ['title','model','full_text','date','price','discount']
