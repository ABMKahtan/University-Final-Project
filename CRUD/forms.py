from django import forms  
from CRUD.models import Portfolio  

class PortfolioForm(forms.ModelForm):  
    class Meta:  
        model = Portfolio  
        fields = "__all__"  