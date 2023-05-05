from django.contrib import admin
from .models import Post
from .models import Contact


class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'status', 'created_on')
  list_filter = ('status',)
  search_fields = ['title', 'content']
  
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
