from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import StockInterest

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
            return redirect("stock_finder")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# 로그아웃 뷰
def logout_view(request):
    logout(request)
    return redirect("login")

# 마이페이지 (관심 종목 리스트)
@login_required
def my_page(request):
    # 관심 종목 추가
    if request.method == "POST":
        stock_name = request.POST.get("stock")
        if stock_name:
            # 중복 방지
            if not StockInterest.objects.filter(user=request.user, stock=stock_name).exists():
                StockInterest.objects.create(user=request.user, stock=stock_name)
            return redirect("accounts:my_page") 
    
    # user 관심 종목들
    interest_stocks = request.user.stock_interests.all()

    context = {
        'interest_stocks' : interest_stocks
    }

    return render(request, 'accounts/my_page.html', context)

# 관심 종목 삭제
@login_required
def stock_delete(request, stock_pk):
    if request.method == "POST":
        stock = StockInterest.objects.get(pk=stock_pk)
        stock.delete()
        return redirect('accounts:my_page')
