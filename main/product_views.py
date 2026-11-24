from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .catalog import CATEGORIES
from .permissions import manager_required

def context_for(model):
    category = model._meta.app_label
    info = CATEGORIES[category]
    return {'category':category, 'category_label':info['label'], 'home_url':info['home'], 'create_url':info['create'], 'detail_url':info['prefix']+'-detail', 'update_url':info['prefix']+'-update', 'delete_url':info['prefix']+'-delete'}

def listing(request, model):
    context = context_for(model)
    context['products'] = model.objects.prefetch_related('images').order_by('-date')
    return render(request, 'main/product_list.html', context)

def detail(request, model, pk):
    context = context_for(model)
    context['product'] = get_object_or_404(model.objects.prefetch_related('images'), pk=pk)
    return render(request, 'main/product_detail.html', context)

@manager_required
@require_http_methods(['GET','POST'])
def edit(request, model, form_class, pk=None):
    product = get_object_or_404(model, pk=pk) if pk is not None else None
    form = form_class(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        with transaction.atomic():
            product = form.save()
            ids = [v for v in request.POST.getlist('remove_photo') if v.isdigit()]
            product.images.filter(pk__in=ids).delete()
            for photo in form.cleaned_data['photos']:
                product.images.create(image=photo)
        return redirect(context_for(model)['detail_url'], pk=product.pk)
    return render(request, 'main/product_form.html', {**context_for(model), 'form':form, 'product':product})

@manager_required
@require_http_methods(['GET','POST'])
def remove(request, model, pk):
    product = get_object_or_404(model, pk=pk)
    context = context_for(model)
    if request.method == 'POST':
        product.delete()
        return redirect(context['home_url'])
    return render(request, 'main/product_delete.html', {**context, 'product':product})
