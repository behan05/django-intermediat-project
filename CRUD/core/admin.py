from django.contrib import admin
from .models import NewUserTB

# Register your models here.

@admin.register(NewUserTB)
class NewUerTbModelAdmin(admin.ModelAdmin):
    list_display = ('id','fname','lname','uname','email','phone','password','cnf_password','data_time')
