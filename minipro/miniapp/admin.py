from django.contrib import admin
from miniapp.models import Register
# Register your models here.
class Registeradmin(admin.ModelAdmin):
    list_display=['id','username','email','gender','phone_number','city','state','pincode']
admin.site.register(Register,Registeradmin) 