from django.urls import path

from center.views import HomeTemplateView, OnAuctionTemplateView, AuctionTableCreateView

app_name = 'center'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('on_auction/', OnAuctionTemplateView.as_view(), name='on_auction'),
    path('product/new/', AuctionTableCreateView.as_view(), name='create_product')

]