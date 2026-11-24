from main.product_forms import ProductForm
from .models import Tv
class TvForm(ProductForm):
    class Meta:
        model = Tv
        fields = ['title','model','full_text','date','price','discount']
