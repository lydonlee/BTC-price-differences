from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Coinexchanges,Coinbar
import tushare as ts

# Create your views here.
class BTCIndexView(generic.ListView):

    template_name = 'btc/BTCindex.html'
    context_object_name = 'BTC_Price_list'

    def get_queryset(self):
        return Coinbar.objects.order_by('m_open')[:10]

def updatecoinbar():
    pro = ts.pro_api()
    exchs = Coinexchanges.objects.all()
    print("exchs:",exchs)
    for exch in exchs:
        try:
            df = pro.Coinbar(exchange=exch.m_exchange, symbol='btcusdt', freq='15min', start_date='20180826', end_date='20180827')
            print("exch.m_exchange=",exch.m_exchange,df["symbol"][0],df["date"][0],df["open"][0])
            onecoin,c = Coinbar.objects.update_or_create(m_coinexchanges = exch,defaults = {'m_symbol':df["symbol"][0], 'm_date':df["date"][0], 'm_open':df["open"][0], 'm_high':df["high"][0],'m_low':df["low"][0], 'm_close':df["close"][0], 'm_vol':df["vol"][0]})
            onecoin.save()
        except Exception as e:
            print('Error', e)
def getexchanges():
    ts.set_token('1360474e70eee70c9c1b9740d684a8800e89903641c6ffb82ac549da')
    pro = ts.pro_api()
    df = pro.Coinexchanges()

    for index,exch in df.iterrows():
        one_exch,created = Coinexchanges.objects.update_or_create(m_exchange=exch["exchange"],defaults ={'m_name':exch["name"]})
        print(exch["name"],exch["exchange"])
        one_exch.save()

def deletemodels():
    Coinexchanges.objects.all().delete()
    Coinbar.objects.all().delete()