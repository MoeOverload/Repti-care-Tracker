from django import forms
from .models import Reptile

class ReptileForm(forms.ModelForm):
    class Meta:
        model = Reptile
        fields = [
            "reptile_name",
            "reptile_species",
            "estimated_age_months",
            "estimated_age_record_date",
        ]