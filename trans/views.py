from django.shortcuts import render
from .models import transaction
from django.db.models import Sum
# Create your views here.
def index(request):
    t = transaction.objects.all()
    last_day = transaction.objects.all().last()

    #sum of cash
    agResult = transaction.objects.aggregate(Sum('cash'))
    cash__sum = agResult['cash__sum']
    
    #sum of ammount recievable
    agResult1 = transaction.objects.aggregate(Sum('accReciev'))
    accReciev__sum = agResult1['accReciev__sum']
    
    #sum of  supplies
    agResult2 = transaction.objects.aggregate(Sum('supplies'))
    supplies__sum = agResult2['supplies__sum']

    #sum of equipment
    agResult3 = transaction.objects.aggregate(Sum('equipment'))
    equipment__sum = agResult3['equipment__sum']

    #sum of ammount payable
    agResult4 = transaction.objects.aggregate(Sum('accPay'))
    accPay__sum = agResult4['accPay__sum']

    #sum of note payable
    agResult5 = transaction.objects.aggregate(Sum('notePay'))
    notePay__sum = agResult5['notePay__sum']

    #sum of owners capital
    agResult6 = transaction.objects.aggregate(Sum('OwnCapital'))
    OwnCapital__sum = agResult6['OwnCapital__sum']

    #sum of owners revenew
    agResult7 = transaction.objects.aggregate(Sum('revenew'))
    revenew__sum = agResult7['revenew__sum']

    #sum of owners drawing
    agResult8 = transaction.objects.aggregate(Sum('drawing'))
    drawing__sum = agResult8['drawing__sum']

    #sum of owners expense
    agResult9 = transaction.objects.aggregate(Sum('expense'))
    expense__sum = agResult9['expense__sum']
       
    if t.exists():
         #Total Asset
        totalAsset = (cash__sum + accReciev__sum + supplies__sum + equipment__sum)
                

        #total libilities and Owner quity
        totalLibOwnEq = accPay__sum + notePay__sum + OwnCapital__sum + revenew__sum +  drawing__sum + expense__sum

        #net income
        net_income = (abs(revenew__sum) - abs(expense__sum))
    else:
        totalAsset = None
        totalLibOwnEq = None
        net_income = None

    
    print(type(t))

    
    


    return render(request, 'index.html', {
        't': t, 
        'last_element': last_day,
        'SumCash': cash__sum, 
        'SumAccRecv': accReciev__sum,
        'SumSupplies': supplies__sum,
        'SumEqup': equipment__sum,
        'SumAccPay': accPay__sum,
        'SumNotePay' : notePay__sum,
        'Sum_OwnCapital': OwnCapital__sum,
        'SumRevenew': revenew__sum,
        'SumDrawing' : drawing__sum,
        'SumExpense': expense__sum,
        'TotalAsset' : totalAsset,
        'TotalLibOwnEq' : totalLibOwnEq,
        'Netincome': net_income


        })