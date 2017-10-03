from django.shortcuts import render
from .models import Blog,Comment,Category
from django.http import Http404
from .forms import CommentForm
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage


def listblogs(request,cate_id = 0):
    '''
    获取 blog 列表
    '''
    if cate_id == 0:
        getblog = Blog.objects.all()
    else:
        try:
            getblog = Blog.objects.filter(category_id=cate_id)
        except Blog.DoesNotExist:
            raise Http404
    # class_id = Category.objects.only('id').get(name = 'Django')
    class_blognum = Blog.objects.raw('SELECT p.id,p.name,COUNT(s.category_id) as count FROM XYZblog_category AS p LEFT JOIN XYZblog_blog AS s ON s.category_id = p.id GROUP BY p.id;')
    after_range_num = 2  # 当前页前显示2页
    befor_range_num = 2  # 当前页后显示2页
    try:  # 如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(getblog, 5)  # 每页显示5
    try:  # 跳转到请求页面，如果该页不存在或者超过则跳转到尾页
        blogs_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        blogs_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    bloglist = {
        'read_rank': Blog.objects.all().order_by("-browser")[:10],  # 获取阅读排行榜
        'class_blognum': class_blognum,
        'blogs':blogs_list,
        'page_range':page_range
    }
    return render(request, 'blog_list.html', bloglist)

def get_detail(request, blog_id):
    '''
    获取 blog 内容
    '''
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        addbrowser = Blog.objects.get(id=blog_id)
        addbrowser.browser += 1
        addbrowser.save()
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    blog_comments = {
        'read_rank' : Blog.objects.all().order_by("-browser")[:10], # 获取阅读排行榜
        'class_blognum': Blog.objects.raw(
            'SELECT p.id,p.name,COUNT(s.category_id) as count FROM XYZblog_category AS p LEFT JOIN XYZblog_blog AS s ON s.category_id = p.id GROUP BY p.id;'),
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
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
