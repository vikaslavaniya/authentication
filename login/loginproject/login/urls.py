from django.urls import path,include
from . import views
urlpatterns=[
path("",views.register,name='home'),
path("login/",views.loginPage,name='login'),
]
