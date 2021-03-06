from django.urls import path

from register.views import RegisterCreateView

app_name = 'register'

urlpatterns = [
        path('', RegisterCreateView.as_view(), name='register')
]