from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('partner',views.Partners_view.as_view(),name='partner'),


]