from django.db import models

# Create your models here.
class transaction(models.Model):
    remark= models.CharField(max_length=50, null=True)
    aDate = models.DateField(auto_now_add=False, default=None)
    cash = models.FloatField(null=True, blank=True, default=0)
    equipment = models.FloatField(null=True, blank=True, default=0)
    supplies = models.FloatField(null=True, blank=True, default=0)
    accReciev = models.FloatField(null=True, blank=True, default=0)
    notePay = models.FloatField(null=True, blank=True, default=0)
    accPay = models.FloatField(null=True, blank=True, default=0)
    OwnCapital = models.FloatField(null=True, blank=True, default=0)
    revenew = models.FloatField(null=True, blank=True, default=0)
    drawing = models.FloatField(null=True, blank=True, default=0)
    expense = models.FloatField(null=True, blank=True, default=0)