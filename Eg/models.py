
# myapp/models.py
from django.db import models
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    age = models.CharField(max_length=15)
    highest_education = models.CharField(max_length=40)
    institute=models.CharField(max_length=40)
    country = models.CharField(max_length=50)
    dept= models.CharField(max_length=20)
    work_exp= models.CharField(max_length=100, null=True)
    inscanada= models.CharField(max_length=100, null=True) 
    POS= models.CharField(max_length=50, null=True)
    feepaid= models.CharField(max_length=50, null=True)
    amount=models.IntegerField(null=True)
    completed_gic=models.CharField(max_length=10, null=True)
    gicamount=models.IntegerField(null=True)
    read = models.IntegerField(null=True) 
    write=models.IntegerField(null=True)
    speak=models.IntegerField(null=True)
    listen=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.full_name
    class Meta:  
        db_table = "UserProfile"

