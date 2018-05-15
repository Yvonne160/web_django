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
