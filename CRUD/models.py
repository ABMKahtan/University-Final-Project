from django.db import models  

class Portfolio(models.Model):  
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    item = models.CharField(max_length=255)  
    item_id = models.CharField(max_length=255)  
    units_owned = models.CharField(max_length=255)  
    ppu_buy = models.CharField(max_length=255)  
    ppu_sell = models.CharField(max_length=255)  
    current_profit = models.CharField(max_length=255)  
    user_id = models.CharField(max_length=10)  

    class Meta:  
        db_table = "portfolio_personaldb"  