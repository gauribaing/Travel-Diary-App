from django import forms
from .models import TripModel
class TripForm(forms.ModelForm):
	class Meta:
		model = TripModel
		fields = "__all__"