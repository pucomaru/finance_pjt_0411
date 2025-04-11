from django.contrib import admin
from django.urls import path, include
from contentfetch import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔹 회원 관련 URL 추가
    path('accounts/', include('accounts.urls')),

    # 🔹 주식 분석 관련
    path('pjt04/index/', views.stock_finder, name='stock_finder'),
    path('pjt04/delete_comment/', views.delete_comment, name='delete_comment'),
    path('pjt04/', RedirectView.as_view(url='/pjt04/index/')),
]
