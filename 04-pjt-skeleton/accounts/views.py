from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.contrib.auth.decorators import login_required
from .models import StockInterest  # ✅ 관심 종목 모델 불러오기


# 회원가입 뷰
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("stock_finder")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

# 로그인 뷰
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("accounts:my_page")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# 로그아웃 뷰
def logout_view(request):
    logout(request)

    return redirect("accounts:login")

# ✅ 관심 종목 목록 조회 및 추가
@login_required
def my_page(request):

    if request.method == "POST":
        stock_name = request.POST.get("stock")
        if stock_name:
            # 중복 방지
            if not StockInterest.objects.filter(user=request.user, stock=stock_name).exists():
                StockInterest.objects.create(user=request.user, stock=stock_name)

        return redirect("accounts:my_page")

    interest_stocks = request.user.stock_interests.all()
    context = {
        "interest_stocks": interest_stocks,
    }
    return render(request, "accounts/my_page.html", context)

# ✅ 관심 종목 삭제 기능 (추가)
@login_required
def stock_delete(request, stock_pk):
    if request.method == "POST":
        stock = StockInterest.objects.get(pk=stock_pk, user=request.user)
        stock.delete()
    return redirect("accounts:my_page")

