from django.contrib import admin

from core.models import Product , CartOrder , Category , Vendor,CartOrderItems , ProductImages ,ProductReview, Wishlists ,Address

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_dispaly = ['user','title','product_image' , 'price', 'featured', 'product_status']


class CategoryAdmin(admin.ModelAdmin):
    list_dispaly = ['title','category_image']

class VendorAdmin(admin.ModelAdmin):
    list_dispaly = ['title','vendor_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_dispaly = ['user','price', 'paid_status', 'order_date','product_status']


class CartOrderItemAdmin(admin.ModelAdmin):
    list_dispaly = ['order','price', 'invoice_no', ' item','image','qty', 'price','total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_dispaly = ['user','product','review','rating']

class wishlistAdmin(admin.ModelAdmin):
    list_dispaly = ['user','product','date']


class AddressAdmin(admin.ModelAdmin):
    list_dispaly = ['user','address','status']



# Register models with their respective admin classes

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlists, wishlistAdmin)
admin.site.register(Address, AddressAdmin)