from django.urls import path
from . import views
app_name = 'userauths'
urlpatterns = [
    path("sign-up/",views.register_view , name="signup"),
    path("sign-in/",views.login_view , name="login"),
    path("sign-out/",views.logout_view , name="logout"),
    
]