from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('product/<slug>', views.ProductDetailsView.as_view(), name="product-details"),

]
