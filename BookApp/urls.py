from django.urls import path
from .import views
from .views import BooklistCreate,BookInfo

urlpatterns=[
    path('listcreate/',BooklistCreate.as_view(),name='list_create'),
    path('bookinfo<int:pk>/',BookInfo.as_view(),name='info'),
]