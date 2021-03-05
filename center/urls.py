from django.urls import path

from center.views import HomeTemplateView

app_name = 'center'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]