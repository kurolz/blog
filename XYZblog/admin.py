from django.contrib import admin

from .models import Category, Tag, Blog, Comment,AdminIMG

class AdminFormTinyMCE(admin.ModelAdmin):
    class Media:
        js=(
            "//cdn.bootcss.com/jquery/2.2.4/jquery.min.js",
            "/static/js/tinymce/jquery.tinymce.min.js",
            "/static/js/tinymce/tinymce.min.js",
            "/static/js/tinymce/textareas.js",
        )
admin.site.register([Blog,Comment,Category,Tag,AdminIMG], AdminFormTinyMCE)