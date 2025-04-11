from django.contrib import admin
from django.urls import path, include # include 추가해서 accouts 랑 url 연결결
from contentfetch import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pjt04/index/', views.stock_finder, name='stock_finder'),
    path('pjt04/delete_comment/', views.delete_comment, name='delete_comment'),
    path('pjt04/', RedirectView.as_view(url='/pjt04/index/')),

    path('accounts/', include('accounts.urls')),
]
