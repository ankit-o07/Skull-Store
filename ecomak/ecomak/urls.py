
from django.contrib import admin
from django.urls import path , include
from core.views import index , base
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',base,name="base"),
    path("",include("core.urls")),
    path("ckeditor/",include("ckeditor_uploader.urls")),
    path("user/",include("userauths.urls"),name="User"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


