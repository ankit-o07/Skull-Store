from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product , CartOrder , Category , Vendor,CartOrderItems , ProductImages ,ProductReview, Wishlists ,Address
# Create your views here.

def index(request):
    products = Product.objects.filter(product_status='published', featured="True")

    context= {
        "products":products
    }

    return render(request,'core/index.html',context)



def product_list_view(request):
    products = Product.objects.filter(product_status='published')

    context= {
        "products":products
    }

    return render(request,'core/product-list.html',context)

def Category_list(request):
    products = Product.objects.filter(product_status='published', featured="True")

    context= {
        "products":products
    }

    return render(request,'core/index.html',context)

def base(request):
    return render(request,"partials/base.html")

