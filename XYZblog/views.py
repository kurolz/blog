# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Blog,Comment,Category,tianqiForm
from django.http import Http404
from .forms import CommentForm,fanyiForm
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage

# 404
def page_not_found(request):
    return render(request,'404.html')
500
# 
def page_error(request):
    return render(request,'500.html')

def listblogs(request,cate_id = 0):
    '''
    获取 blog 列表
    '''
    if cate_id == 0:
        getblog = Blog.objects.all().order_by('-created')
    else:
        try:
            getblog = Blog.objects.filter(category_id=cate_id).order_by('-created')
        except Blog.DoesNotExist:
            raise Http404
    # 翻译 #
    fanyi_dict = {}
    fanyi_form = fanyiForm()
    if request.method == 'POST':
        fanyi_form = fanyiForm(request.POST)
        if 'tianqi' in request.POST:
            shuaxinTianqi()
        if fanyi_form.is_valid():
            fanyi_dict = youdaofanyi(request)
        # 搜索 #
        if 'header_search' in request.POST:
            search_speech = request.POST.get('search','')
            getblog = Blog.objects.filter(title__icontains=search_speech) 
            
            
    class_blognum = wenzhangfenlei()  # 获取博客分类
    after_range_num = 2  # 当前页前显示2页
    befor_range_num = 2  # 当前页后显示2页
    try:  # 如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(getblog, 10)  # 每页显示5
    try:  # 跳转到请求页面，如果该页不存在或者超过则跳转到尾页
        blogs_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        blogs_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]


    #     #
    read_rank = readrank()  # 获取阅读排行榜
    tianqi_info = gettianqi() # 获取天气信息
    bloglist = {
        'read_rank': read_rank,  # 获取阅读排行榜
        'class_blognum': class_blognum, # 博客分类
        'blogs':blogs_list, # 博客列表
        'page_range' : page_range, # 分页
        'tianqi_info' : tianqi_info, # 天气
        'fanyi_form' : fanyi_form, # 翻译的表单
        'fanyi_dict' : fanyi_dict, # 翻译出来的文本
    }
    return render(request, 'blog_list.html', bloglist)

def get_detail(request, blog_id):
    '''
    获取 blog 内容
    '''
    fanyi_dict = {}
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        addbrowser = Blog.objects.get(id=blog_id)
        addbrowser.browser += 1
        addbrowser.save()
        fanyi_form = fanyiForm()
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
            sendMail(str(blog),cleaned_data['name'])
    # 翻译 #
        fanyi_form = fanyiForm(request.POST)
        if fanyi_form.is_valid():
            fanyi_dict = youdaofanyi(request)
    #     #
    read_rank = readrank()  # 获取阅读排行榜
    class_blognum = wenzhangfenlei()    # 获取博客分类
    tianqi_info = gettianqi() # 获取天气信息
    blog_comments = {
        'read_rank' : read_rank, # 阅读排行
        'class_blognum': class_blognum, # 博客分类
        'blog': blog,   # 博客信息
        'comments': blog.comment_set.all().order_by('-created'),    # 获取评论信息
        'fanyi_form': fanyi_form,   # 翻译的表单
        'tianqi_info' : tianqi_info,
        'form': form,   # 评论的表单
        'fanyi_dict': fanyi_dict, # 翻译出来的文本
    }
    return render(request, 'blog_detail.html', blog_comments)

from .models import AdminIMG
def uploadIMG(request):
    '''
    admin 上传图片
    返回图片，使得图片可以直接显示在输入框中
    '''
    img = request.FILES.get('img')
    adminIMG = AdminIMG()
    adminIMG.filename = img.name
    adminIMG.img = img
    adminIMG.save()
    return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('/media/%s').closest('.mce-window').find('.mce-primary').click();</script>" % adminIMG.img)

def readrank():
    '''
    获取阅读排行
    '''
    read_rank = Blog.objects.all().order_by("-browser")[:10]
    return read_rank

def  wenzhangfenlei():
    '''
    获取博客分类
    '''
    fenlei = Blog.objects.raw('SELECT p.id,p.name,COUNT(s.category_id) as count FROM XYZblog_category AS p LEFT JOIN XYZblog_blog AS s ON s.category_id = p.id GROUP BY p.id;')
    return fenlei

def youdaofanyi(request):
    '''
    有道翻译功能
    '''
    import json
    from urllib import parse
    import urllib.request, urllib.parse, urllib.request
    query = {}  # 定义需要翻译的文本
    fanyi = request.POST.get('fanyi_content', '')
    query['q'] = fanyi  # 输入要翻译的文本
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&' + parse.urlencode(
        query)  # 有道翻译api
    response = urllib.request.urlopen(url, timeout=3)

    # 编码转换
    try:
        html = response.read().decode('utf-8')
        d = json.loads(html)
        explains = d.get('basic').get('explains')  # 翻译后输出
        a1 = d.get('basic').get('uk-phonetic')  # 英式发音
        a2 = d.get('basic').get('us-phonetic')  # 美式发音
        explains_list = []
        for result in explains:
            explains_list.append(result)
        # 输出
        fanyi_dict = {
            'q': query['q'],
            'yinshi': a1,
            'meishi': a2,
            'explains_list': explains_list,
        }
        return fanyi_dict
    except Exception as e:
        print (e)

import os
def shuaxinTianqi():
    '''
    启动抓取天气信息爬虫
    :return:
    '''
    os.system("cd /code/blog/weather && scrapy crawl tianqi")

def gettianqi():
    '''
    获取天气信息
    '''
    tianqi_info = tianqiForm.objects.all()
    return tianqi_info

def sendMail(blog,content):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置smtp服务器，例如：smtp.163.com
    mail_user = "kurolz@163.com"  # 发送的邮箱用户名
    mail_pass = "******"  # 发送的邮箱密码

    sender = 'kurolz@163.com'  # 发送的邮箱
    receivers = 'kurolz@163.com'  # 接收的邮箱
    text = '博客《' + blog + ' 》收到【' + content + '】的评论'
    message = MIMEText(text)
    message['From'] = sender
    message['To'] = receivers

    subject = text
    message['Subject'] = Header(subject)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)    # login
        smtpObj.sendmail(sender, receivers, message.as_string())    # 发送邮件
        result = "邮件发送成功"
    except smtplib.SMTPException as e:
        result = "Error: 无法发送邮件" + str(e)
    return result
