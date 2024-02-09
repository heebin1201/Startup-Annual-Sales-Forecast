from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('predict/', views.predict),
    path('createform/', views.createform),
    # path('createform/createform', views.createform, name='createform')
]