from django.db import models
from merchants.models import Merchant

class Beneficiary(models.Model):
    unique_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    merchant = models.ForeignKey(Merchant, related_name='beneficiaries')