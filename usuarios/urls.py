from django.urls import path
from django.views import login

urlpatterns = [
    path('login/', login, name='login')
    
]
