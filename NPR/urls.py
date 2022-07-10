from . import views 
from django.urls import path 

urlpatterns = [
    path('', views.NPRAPIView.as_view(), name='article' )
]