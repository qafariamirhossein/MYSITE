from django.contrib import admin
from blog.models import Post,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    pass
    empty_value_display = 'Null'
    list_filter = ('author','status')
    list_display = ('title','author','status','created_date')

admin.site.register(Category)
admin.site.register(Post,PostAdmin) 