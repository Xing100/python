from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
# Create your views here.

def my_render(request,template_path,context_dict):
    '''使用模板文件'''
    # 1.加载模板文件，模板对象
    temp = loader.get_template(template_path)
    # 2，定义模板上下文:给模板文件传递数据
    context = RequestContext(request, context_dict)
    # 3.模板渲染:产生标准的html内容
    res_html = temp.render(context)
    # 4.返回给浏览器
    return HttpResponse(res_html)

# 定义视图函数
def index(request):
    #进行处理，和m和t进行交互
    # return my_render(request,'booktest/index.html',{})
    return render(request,'booktest/index.html',{'content':'hello python'})




def like(request):
    return HttpResponse('like')



"""
视图函数的使用
1.定义视图函数
视图函数必须一个参数request，进行处理之后，需要返回一个HttpResponse的类对象，
里面的参数就是返回给浏览器显示的内容
2，进行url配置
配置url时，有两种语法格式
url(正则表达式，视图函数名)
url(正则表达式，include(应用中的urls文件))


{{模板变量名}}
模板代码段：{%代码段%}
"""


