from demo import views
from django.urls import path

urlpatterns = [
    path('login/', views.login),
    path('login_check/',views.login_check),
    path('logon/',views.logon),
    path('test_ajax/',views.test_ajax),
    path('ajax_test/',views.ajax_test)
]
