from django.urls import path

from . import views

app_name = 'btc'
urlpatterns = [
    path('', views.BTCIndexView.as_view(), name='BTCindex')
]