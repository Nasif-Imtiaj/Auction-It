from django.urls import path

from center.views import HomeTemplateView, OnAuctionListView, AuctionTableCreateView, AuctionTableUpdateView, \
    AuctionTableDetailView, AuctionTableDeleteView, UserItemsListView, BettersCreateView

app_name = 'center'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('on_auction/', OnAuctionListView.as_view(), name='on_auction'),
    path('my_items/', UserItemsListView.as_view(), name='my_items'),
    path('<int:pk>/', AuctionTableDetailView.as_view(), name='detail_product'),
    path('product/new/', AuctionTableCreateView.as_view(), name='create_product'),
    path('Bet/new/', BettersCreateView.as_view(), name='betters'),
    path('<int:pk>/update/', AuctionTableUpdateView.as_view(), name='update_product'),
    path('<int:pk>/delete/', AuctionTableDeleteView.as_view(), name='product_confirm_delete')

]