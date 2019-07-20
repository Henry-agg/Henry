from django.shortcuts import render
from demo.models import bookinfo
# Create your views here.
'''
4）定义视图中的方法，实现添加图书的功能（10分）
5）定义视图中的方法，实现根据book_id实现查找图书功能（10分）
6）定义视图中的方法，实现根据图书名称查找图书的功能（10分）
7）正确启动服务器（10分）
8）查询图书信息，把所有图书信息显示在浏览器上（10分）
9）查询图书编号小于5的图书信息，并显示在浏览器上（10分）
10）查询图书名称中包含‘部’的所有图书，显示在浏览器上（10分）
'''
def insert(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        book_gender = request.POST.get('book_gender')
        book_id = request.POST.get('book_id')
        bcontent = request.POST.get('bcontent')
        bookinfo.objects.create(bookname=bookname,book_gender=book_gender,book_id=book_id,bcontent=bcontent)
        e = '添加图书信息成功！'
        return render(request, 'Index.html', {'e':e})
    return render(request,'Insert.html')

def select_book_id(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        a = bookinfo.objects.get(book_id=book_id)
        e = str(a.bookname)
        return render(request, 'Index.html', {'e':e})
    return render(request, 'Select_book_id.html')

def select_bookname(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        a = bookinfo.objects.get(bookname=bookname)
        e = str(a.book_id)
        return render(request, 'Index.html', {'e':e})
    return render(request, 'Select_bookname.html')

def select_all(request):
    a = bookinfo.objects.all()
    return render(request,'Select_all.html',{'a':a})

def select_lt(request):
    a = bookinfo.objects.filter(book_id__lt=5)
    return render(request,'Select_lt.html',{'a':a})

def select_contains(request):
    a = bookinfo.objects.filter(bookname__contains='部')
    return render(request,'Select_contains.html',{'a':a})