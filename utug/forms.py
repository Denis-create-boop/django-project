from main.product_forms import ProductForm
from .models import Utug
class UtugForm(ProductForm):
    class Meta:
        model = Utug
        fields = ['title','model','full_text','date','price','discount']
