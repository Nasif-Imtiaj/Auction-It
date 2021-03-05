from django.urls import path

from core.views import HomeTemplateView, AboutTemplateView, OnAuctionTemplateView, ItemCreateView

app_name = 'core'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('on_auction/', OnAuctionTemplateView.as_view(), name='on_auction'),
    path('item/new/', ItemCreateView.as_view(), name='create-item')
]