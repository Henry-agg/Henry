from django.contrib import admin
from demo.models import backstage
# Register your models here.
@admin.register(backstage)
class backstageadmin(admin.ModelAdmin):
    list_display = ['id','username','password']
