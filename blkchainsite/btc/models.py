from django.db import models
import datetime
from django.utils import timezone


class Coinexchanges(models.Model):
    m_exchange = models.CharField(max_length=10)
    m_name = models.CharField(max_length=20)
    m_area = models.CharField(max_length=10,default="unknown")
    m_website = models.CharField(max_length=20)

    def __str__(self):
        return self.m_name


class  Coinbar(models.Model):
    m_coinexchanges = models.ForeignKey(Coinexchanges, on_delete=models.CASCADE)

    m_symbol = models.CharField(max_length=10)
    m_date = models.DateTimeField()
    m_open = models.FloatField(default=0)
    m_high = models.FloatField(default=0)
    m_low = models.FloatField(default=0)
    m_close = models.FloatField(default=0)
    m_vol = models.FloatField(default=0)

    def __str__(self):
        return self.m_symbol

# Create your models here.
