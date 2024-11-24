from django.urls import path
from .views import store_home,product_detail


urlpatterns = [
    path("",store_home,name="store"),
    path("<slug:category_slug>",store_home, name="products_by_category"),
    path("<slug:category_slug>/<slug:product_slug>/",product_detail, name="product_detail")
]




