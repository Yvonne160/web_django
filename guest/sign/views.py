from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 

# #django 简单返回
# def index(request):
#      return HttpReponse("hello django!")


# #Django 模板返回
# def index(request):
#      return render(request,'index.html')


# #Get 请求
# def index(request):
#     return render(request,'index.html')


#post 请求
def index(request):
    return render(request,'index.html')


#处理登录请求
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('user','')
        password = request.POST.get('pw','')
        if username=="admin" and password=="admin123":
            return HttpResponse('login success!')
        else:
            return render(request,'index.html',{'error':'用户名或密码错误'})

