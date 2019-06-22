from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name="create"),
    path('items/<int:pk>/delete', views.DeleteItem.as_view(), name="items_delete"),
]