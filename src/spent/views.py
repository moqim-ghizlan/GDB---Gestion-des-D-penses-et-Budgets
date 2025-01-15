from django.shortcuts import render, redirect
from spent.models import Spent
from datetime import date
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login')
def index(request):
    spents = Spent.objects.filter(month = Spent.CURRENT_MONTH, user=request.user)
    get_current_month_local = Spent.MONTHS[Spent.CURRENT_MONTH-1][1]
    res = 0
    for sp in spents:
        res += sp.amount
    return render(request, 'index.html', {'spents': spents, 'get_current_month_local':get_current_month_local, 'get_month_spents' : round(res, 2)})




@login_required(login_url='/accounts/login')
def create(request):
    if request.method == "POST":
        done_at = request.POST['done_at']
        title = request.POST['title']
        description = request.POST['description']
        amount = request.POST['amount']
        month = request.POST['month']
        spent = Spent.objects.create(
            done_at=done_at,
            title=title,
            description=description,
            amount=amount,
            month=month,
            user=request.user
        )
        return redirect('spent:index')
    return render(request, 'index.html', {})





@login_required(login_url='/accounts/login')
def update(request, id):
    spent = Spent.objects.filter(id=id).first()
    if not spent:
        return redirect('spent:index')
    if request.method == "POST":
        done_at = request.POST['done_at']
        title = request.POST['title']
        description = request.POST['description']
        amount = request.POST['amount']
        month = request.POST['month']
        print('done_at', done_at)
        spent.done_at = done_at
        spent.title = title
        spent.description = description
        spent.amount = amount
        spent.month = month
        spent.save()
        return redirect('spent:index')
    return render(request, 'index.html', {})





@login_required(login_url='/accounts/login')
def delete(request, id):
    spent = Spent.objects.filter(id=id).first()
    if not spent:
        return redirect('spent:index')
    spent.delete()
    return redirect('spent:index')

@login_required(login_url='/accounts/login')
def spents_by_month(request, id):
    month = Spent.MONTHS[id-1][1]
    spents = Spent.objects.filter(month=id, user=request.user)
    res = 0
    for sp in spents:
        res += sp.amount
    return render(request, 'index.html', {'spents': spents, 'get_current_month_local':month, 'get_month_spents' : round(res, 2)})
