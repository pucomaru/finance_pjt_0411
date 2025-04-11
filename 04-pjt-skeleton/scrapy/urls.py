from django.contrib import admin
from django.urls import path, include
from contentfetch import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # accounts 앱은 네임스페이스 설정 포함
    path("accounts/", include("accounts.urls", namespace="accounts")),

    # contentfetch 앱은 깔끔하게 별도 include
    path('contentfetch/', include('contentfetch.urls')),

    # 주식 분석 기능 직접 연결
    path("pjt04/index/", views.stock_finder, name="stock_finder"),
    path("pjt04/delete_comment/", views.delete_comment, name="delete_comment"),
    path("pjt04/", RedirectView.as_view(url='/pjt04/index/')),
    
    # 기본 루트는 주식 분석으로 리디렉트
    path("", RedirectView.as_view(url='/pjt04/index/')),
]
