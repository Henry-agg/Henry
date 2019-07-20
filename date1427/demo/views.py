from django.shortcuts import render
from demo.models import backstage
from django.http import HttpResponse,JsonResponse
# Create your views here.
def login(request):
    return render(request,'Login.html')
error = ''

def login_check(request):
    users = backstage.objects.all()
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    d = {}
    for i in users:
        d[i.username] = i.password
    if username not in d:
        error = '用户名错误'
        return render(request,'Login.html',{'error':error})
    elif pwd != str(d[username]):
        error = '密码错误'
        return render(request, 'Login.html', {'error': error})
    else:
        return render(request,'Index.html',{'username':username})

def logon(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        backstage.objects.create(username=username,password=pwd)
        return HttpResponse('注册成功')
    return render(request,'Logon.html')

def test_ajax(request):
    return render(request,'Test_ajax.html')

def ajax_test(request):
    return JsonResponse({'res':1})