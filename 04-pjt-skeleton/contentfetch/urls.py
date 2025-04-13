from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

app_name = 'contentfetch'

urlpatterns = [
    path("", views.stock_finder, name="stock_finder"),
    path("delete_comment/", views.delete_comment, name="delete_comment"),
    # path("", RedirectView.as_view(url='/pjt04/index/')),
]
