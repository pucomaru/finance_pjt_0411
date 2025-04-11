# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path('my_page/', views.my_page, name='my_page'),
    path('<int:stock_pk>/stock_delete/', views.stock_delete, name='stock_delete'),
]
