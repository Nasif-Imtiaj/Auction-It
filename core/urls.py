from django.urls import path

from core.views import HomeTemplateView, AboutTemplateView, ItemCreateView

app_name = 'core'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('item/new/', ItemCreateView.as_view(), name='create-item')
]