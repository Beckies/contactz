from django.db import models
from accounts.models import Organization
#from django.conf import settings

class Merchant(models.Model):
	#user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	unique_id = models.IntegerField(default=0)
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	organization = models.ForeignKey(Organization, related_name='merchants')

