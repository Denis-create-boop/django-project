from main.product_forms import ProductForm
from .models import Muse
class MuseForm(ProductForm):
    class Meta:
        model = Muse
        fields = ['title','model','full_text','date','price','discount']
