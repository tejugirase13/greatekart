from django.shortcuts import render, get_object_or_404
from store.models import Product
from Category.models import Category


def store_home(request, category_slug=None):
    category = None
    product = None
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()


    context = {"products": products, "product_count": products_count}

    return render(request, 'store.html', context)


def product_detail(request, category_slug=None, product_slug=None):
    try:
        if product_slug:
            product_slug = product_slug.lower()
            single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)

    except Exception as e:
        raise e


    context = {'single_product':single_product}

    return render(request, "product_detail.html",context)



