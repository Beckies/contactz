from django import forms
from .models import Merchant

class MerchantForms(forms.ModelForm):
	class Meta:
		model = Merchant
