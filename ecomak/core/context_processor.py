from core.models import Product , CartOrder , Category , Vendor,CartOrderItems , ProductImages ,ProductReview, Wishlists ,Address
from django.db.models import Min, Max

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price = Product.objects.aggregate(Min("price"),Max("price"))
    

    print(request.user)
    try:
        address = Address.objects.filter(user = request.user.id).first()
    except:
        address = None

    return {
        'categories' : categories,
        'address':address,
        'vendors':vendors,
        'min_max_price':min_max_price,
    }