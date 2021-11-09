from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Stock, Watchlist

  

@login_required(login_url='login')
def watchlist_view(request):
    res = request.user.id
    result = Watchlist.objects.filter(userid=res)
    arr=[]
    for i in result:
        fresult = Stock.objects.filter(stockid=i.stockid)
        arr.append(fresult)
    return render(request, 'watchlist.html',{'watchlist':arr})


def watchlist_delete(request,id):
    stock = Watchlist.objects.get(stockid = id)
    stock.delete()
    stock.save()
    return HttpResponse('Stock is successfully removed from your watchlist.')

def search_wl(request):
    wlstockid = request.GET.get('wlstockid')
    error_msg = ''
    if not wlstockid:
        error_msg = 'Please input a stock ID'
        print(error_msg)
    search_list = Stock.objects.get(stockid = wlstockid)
    return render(request, 'wlresults.html', {'search_list': search_list})


def watchlist_add(request,stockid):
    b = Watchlist(userid=request.user.id,stockid=stockid)
    b.save()
    return HttpResponse("Stock is successfully added in your watchlist.")

    stock.delete()
    stock.save()
    return HttpResponse('Stock is successfully removed from your watchlist.')
