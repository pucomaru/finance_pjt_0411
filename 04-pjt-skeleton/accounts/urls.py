from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('my_page/',views.my_page,name='my_page'),
    path('<int:stock_pk>/stock_delete/',views.stock_delete,name='stock_delete'),
]
