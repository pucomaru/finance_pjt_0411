from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  # ✅ 이 이름과 views.py 안의 함수 이름을 맞춰야 해!
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
