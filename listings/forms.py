from django import forms  
from listings.models import Personaldb

class PortfolioForm(forms.ModelForm):  
    class Meta:  
        model = Personaldb  
        fields = "__all__"  