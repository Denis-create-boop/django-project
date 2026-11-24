from main.product_forms import ProductForm
from .models import Computer
class ComputerForm(ProductForm):
    class Meta:
        model = Computer
        fields = ['title','model','full_text','date','price','discount']
