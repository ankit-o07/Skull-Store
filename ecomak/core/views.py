from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , JsonResponse
from core.models import Product , CartOrder , Category , Vendor ,CartOrderItems , ProductImages ,ProductReview, Wishlists ,Address
from django.db.models import Count , Avg
from taggit.models import Tag
from .forms import ProductReviewForm
from django.template.loader import render_to_string

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



def category_list(request):
    categories = Category.objects.all()

    context= {
        "categories":categories
    }

    return render(request,'core/category-list.html',context)

 
def category_product_list_views(request,cid):
    category = Category.objects.get(cid=cid)
    products  = Product.objects.filter(product_status="published",category=category)
 
    context = {
        "category":category,
        "product":products
    }
    return render(request , "core/category-product-list.html",context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors" : vendors,
    }

    return render(request,"core/vendor_list.html",context)


def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid = vid)
    products = Product.objects.filter(vendor=vendor ,product_status="published" )
    context = {
        "vendor" : vendor,
        "products" : products
    }

    return render(request,"core/vendor_detail.html",context)


def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product,pid=pid)
    products = Product.objects.filter(category = product.category).exclude(pid=pid)
    p_image = product.p_image.all()

    reviews= ProductReview.objects.filter(product=product)
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))


    # Product Review form
    review_form = ProductReviewForm()

    context = {
        "product":product,
        "products":products,
        "reviews": reviews,
        "average_rating" : average_rating ,
        'review_form': review_form,
    }
    
    
    return render (request, "core/product_detail.html",context)

def tag_list(request,tag_slug=None):
    products  = Product.objects.filter(product_status="published",)
    tag = None 
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
    
    context= {
        "products":products
    }

    return render(request,'core/tag.html',context)
    


def ajax_add_review(request,pid):
    
    product = Product.objects.get(pid = pid)
    user = request.user
    

    review = ProductReview.objects.create(
        user=user,
        product = product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        "rating" : request.POST['rating'],


    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))

    return JsonResponse(
        {
            'bool':True,
            'context':context,
            'average_reviews':average_reviews,
        }

 
    )


def search_view(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query, description__icontains=query).order_by("-date")

    context = {
        "products" :products,
        "query": query,
    }

    return  render(request,'core/search.html',context)

def filter_product(request):
    categories = request.GET.getlist('category[]')
    vendors = request.GET.getlist('vendor[]')

    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    products = Product.objects.filter(product_status='published').order_by("-id").distinct()
    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)


    if len(categories) >0:
        products = products.filter(category__id__in = categories).distinct()

    if len(vendors) >0:
        products = products.filter(vendor__id__in = vendors).distinct()

    
    data  = render_to_string("core/asyn/product_list.html",{"products":products})
    print(data)
    return JsonResponse({"data":data})


def add_to_cart(request):
    print("View is called")
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title' : request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
    }
    print("View is called no 2")
    if 'cart_data_obj' in request.session:
        print("View is called no 3")
        if str(request.GET['id']) in request.session['cart_data_obj']:
            print("View is called no 4")
            cart_data= request.session['cart_data_obj']
            # cart_data[str(request.GET['id'])]["qty"] = int(cart_product[str(request.GET['id']['qty'])])
            cart_data[str(request.GET['id'])]["qty"] = int(request.GET['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else: 
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data":request.session['cart_data_obj'],'totalcartitem':len(request.session['cart_data_obj'])})



def cart_view(request):
    cart_total_amount = 0 
    if 'cart_data_obj'  in request.session:
        for p_id , item  in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "core/cart.html")
    else : 
        return render(request, "core/cart.html")


def base(request):
    return render(request,"partials/base.html")



 

