from django.db import models

# Create your models here.
class NewUserTB(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    uname = models.CharField(max_length=70)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    cnf_password = models.CharField(max_length=30)
    data_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fname
    
    
