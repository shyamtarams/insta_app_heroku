from django.urls import path
from . import views 

urlpatterns = [
    path('index',views.indexfn, name="index"),
    path('about2',views.fn1),
    path('i2',views.fn2),
]