from django.urls import path
from .views import *

urlpatterns = [
    path('django_sign_up/', sign_up_by_django),
    path('html_sign_up/', sign_up_by_html),
]