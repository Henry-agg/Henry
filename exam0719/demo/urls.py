from django.urls import path
from demo import views

urlpatterns = [
    path('insert/', views.insert),
    path('select_book_id/',views.select_book_id),
    path('select_bookname/',views.select_bookname),
    path('select_all/', views.select_all),
    path('select_lt/', views.select_lt),
    path('select_contains/', views.select_contains),
]
