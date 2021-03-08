from django.urls import path

from accounts.views import StatusTemplateView

app_name = 'accounts'

urlpatterns = [
    path('status/', StatusTemplateView.as_view(), name='status')
]