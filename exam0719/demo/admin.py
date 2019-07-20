from django.contrib import admin
from demo.models import bookinfo
# Register your models here.
@admin.register(bookinfo)
class bookinfoadmin(admin.ModelAdmin):
    list_display = ['id','bookname','book_gender','book_id','bcontent']