from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse



# Create your views here.

def index(request):

    return render(request,'booktest/index.html')


def login(request):

    return render(request,'booktest/login.html')



def login_check(request):
    # reqeust.POST 保存的是post方式提交的参数
    # request.GET 保存的是get方式提交的参数
    # 获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # # 进行登录校验
    if username == '123' and password == '123':
        return redirect('/index')
    else:
        return redirect('/login')

    # 返回应答
