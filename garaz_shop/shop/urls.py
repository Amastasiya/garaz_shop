from django.urls import path
from .views import ProductDetailView

from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('shop/<str:ct_model>/<str:ssylka>', ProductDetailView.as_view(), name='product_detail' )

]
