from django.db import models
# from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    """
    分类
    """
    name = models.CharField('名称', max_length=16)
    def  __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签
    """
    name = models.CharField('名称', max_length=16)
    def  __str__(self):
        return self.name

class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=100)
    author = models.CharField('作者', max_length=16)
    description = models.CharField('描述', max_length=200)
    content = models.TextField(blank=True, null=True,verbose_name="正文")
    created = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    browser = models.IntegerField('浏览量',editable=False,default=0)



    def  __str__(self):
        return self.title

class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def  __str__(self):
        return self.content

class AdminIMG(models.Model):
    filename = models.CharField(max_length=200, blank=True, null=True)
    img  = models.ImageField(upload_to = './admin')

    def  __str__(self):
        return self.filename

class tianqiForm(models.Model):
    chengshi = models.CharField(u'城市',max_length=100)
    date = models.CharField(u'日期',max_length=30)
    img = models.CharField(u'图片',max_length=200)
    temperature = models.CharField(u'温度',max_length=30)
    cloud = models.CharField(u'云',max_length=20)
    wind = models.CharField(u'风',max_length=20)

    def  __str__(self):
        return self.chengshi
