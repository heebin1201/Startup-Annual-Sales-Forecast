from django.shortcuts import render,redirect
from .models import project,Alert_history,predict_a

# Create your views here.
#edit
from django.http import HttpResponse

def home(request):
    
    return render(request, 'home.html' )


def predict(request):
    if request.method == 'GET':
        return render(request, 'predict.html')

def createform(request):

    invest = request.GET.get('invest')
    address = request.GET.get('address')
    people = request.GET.get('people')
    leave = request.GET.get('leave')
    invest_cnt = request.GET.get('invest_cnt')
    money_MO = request.GET.get('money_MO')
    invest_money = request.GET.get('invest_money')
    money_sale = request.GET.get('money_sale')
    money_sales = request.GET.get('money_sales')
    money_net = request.GET.get('money_net')
    money_nets = request.GET.get('money_nets')
    asset = request.GET.get('asset')
    asset_a = request.GET.get('asset_a')
    capital = request.GET.get('capital')
    capital_a = request.GET.get('capital_a')
    sale = request.GET.get('sale')
    sales = request.GET.get('sales')
    invest_recent = request.GET.get('invest_recent')
    capital_erosion = request.GET.get('capital_erosion')
    year = request.GET.get('year')
    service = request.GET.get('service')
    invest_count = request.GET.get('invest_count')
    scale = request.GET.get('scale')


    # context = {
    #     'invest':invest,
    # 	'money':money,
    #     'moneya':moneya,
    #     'moneyb':moneyb,
    #     'moneyc':moneyc,
    #     'employee':employee    
    # } 
    class_object = predict_a.objects.all()
    for ii in class_object:
        if ii.a == (invest) and ii.b == (address) and ii.c == int(people) and ii.d == int(leave) and ii.e == int(invest_cnt)and ii.f == int(money_MO) and ii.g == int(invest_money) and ii.h == int(money_sale) and ii.i == int(money_sales):
            a = 51
            c = 6984
   
    # print(type(money))

    return render(request, 'form_create.html', {'a':a, 'c':c} )