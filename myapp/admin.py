from django.contrib import admin
from .models import *

# Register your models here.
class signupData(admin.ModelAdmin):
    list_display=['id','created','firstname','lastname','username','city','mobile']

admin.site.register(userSignup,signupData)


class notesData(admin.ModelAdmin):
    list_display=['id','title','cate','myfile','desc']

admin.site.register(mynotes,notesData)