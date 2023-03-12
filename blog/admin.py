from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    empty_value_display = 'Null'
    list_filter = ('author','status')
    list_display = ('title','author','login_require','status','created_date')



class CommentAdmin(admin.ModelAdmin):
    empty_value_display = 'Null'
    list_filter = ('post','approve')
    list_display = ('post','name','approve','created_date')




admin.site.register(Category)
admin.site.register(Post,PostAdmin) 
admin.site.register(Comment,CommentAdmin)