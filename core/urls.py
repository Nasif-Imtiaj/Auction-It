from django.urls import path

from core.views import HomeTemplateView, AboutTemplateView, ItemCreateView, MembersListView

app_name = 'core'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('item/new/', ItemCreateView.as_view(), name='create-item'),
    path('members/', MembersListView.as_view(), name='members')
]