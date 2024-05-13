from django.urls import path , include

from core.views import index , product_list_view , category_list , category_product_list_views , vendor_list_view, vendor_detail_view , product_detail_view , tag_list , ajax_add_review , search_view , filter_product , add_to_cart , cart_view

app_name='core'
urlpatterns=[
    # Homepage
    path("",index, name="index"),
    path("products/",product_list_view,name='product_list'),
    path("product/<pid>",product_detail_view,name="product_detail"),

    # Category
    path("category/",category_list,name='category_list'),
    path("category/<cid>/",category_product_list_views,name='category_product_list'),  
    
    # vendor 
    path("vendor/",vendor_list_view,name="vendor_list"),
    path("vendor/<vid>", vendor_detail_view,name="vendor_details"),

    #Tags

    path("products/tag/<tag_slug>/",tag_list , name="tags"),

    # Add reviews

    path('ajax-add-review/<pid>/', ajax_add_review,name='ajax_add_review'),

    # search

    path('search/', search_view , name="search"),

    # Filter Product URL 
    path("filter-product",filter_product ,name="filter_product" ),

    # add to cart URL
    path("add-to-cart/", add_to_cart , name="add_to_cart"),

    # cart page url 
    path("cart/", cart_view , name="cart_view"),
]
