from django.urls import path
from .views import func_view, ClassView

urlpatterns = [
    path('func_view/', func_view),
    path('class_view/', ClassView.as_view()),
]