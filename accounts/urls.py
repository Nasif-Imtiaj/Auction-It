from django.urls import path

from accounts.views import StatusTemplateView, ProfileTemplateView

app_name = 'accounts'

urlpatterns = [
    path('status/', StatusTemplateView.as_view(), name='status'),
    path('profile/', ProfileTemplateView.as_view(), name='profile'),
]