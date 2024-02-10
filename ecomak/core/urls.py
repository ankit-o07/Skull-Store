from django.urls import path , include

from core.views import index , product_list_view , Category_list 

app_name='core'
urlpatterns=[
    path("",index, name="index"),
    path("products/",product_list_view,name='product_list'),
    path("category/",product_list_view,name='category_list'),
    
    
    
]