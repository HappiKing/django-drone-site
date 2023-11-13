from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('product/', views.product),
    path('product/option/', views.product_option),
    path('support/', views.support),

]