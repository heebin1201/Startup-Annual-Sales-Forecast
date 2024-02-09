from django.db import models

# Create your models here.
class project(models.Model):
    money = models.IntegerField()
    moneya = models.IntegerField()
    moneyb = models.IntegerField()
    moneyc = models.IntegerField()
    employee = models.IntegerField()
   

class Alert_history(models.Model):
    date = models.FloatField()
    alert_rating = models.FloatField()
    alert_g_spread = models.FloatField()
    alert_bm_spread = models.FloatField()
    alert_ai = models.FloatField()
    alert = models.FloatField()
    total = models.FloatField()
    region= models.FloatField()

class predict_a(models.Model):
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.FloatField()
    d = models.FloatField()
    e = models.FloatField()
    f = models.FloatField()
    g = models.FloatField()
    h = models.FloatField()
    i = models.FloatField()
    j = models.FloatField()
    k = models.FloatField()
    l = models.FloatField()
    m = models.FloatField()
    n = models.FloatField()
    o = models.FloatField()
    p = models.FloatField()
    q = models.FloatField()
    r = models.FloatField()
    s = models.FloatField()
    t= models.FloatField()
    u= models.FloatField()
    v= models.FloatField()
    w= models.FloatField()
    