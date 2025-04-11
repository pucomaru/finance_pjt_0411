from django.shortcuts import render, redirect
from .models import StockInterest

# Create your views here.

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
    interest_stocks = user.stock_interests.all()

    context = {
        'interest_stocks' : interest_stocks
    }

    return render(request,'accounts/my_page.html',context)

def stock_delete(request,stock_pk):
    if request.method == "POST":
        stock = StockInterest.objects.get(pk=stock_pk)
        stock.delete()
        return redirect('accounts:my_page')
        
