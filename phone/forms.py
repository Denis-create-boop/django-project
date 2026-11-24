from main.product_forms import ProductForm
from .models import Phone
class PhoneForm(ProductForm):
    class Meta:
        model = Phone
        fields = ['title','model','full_text','date','price','discount']
