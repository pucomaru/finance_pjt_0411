from django.contrib import admin
from django.urls import path, include
from contentfetch import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", RedirectView.as_view(url='/pjt04/index/')),  # 홈 접근 시 자동 리디렉트
    path('contentfetch/',include('contentfetch.urls')),

]
