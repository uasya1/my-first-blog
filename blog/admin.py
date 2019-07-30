from django.contrib import admin
from .models import Post, Comment, PostStatistic

admin.site.register(Post)
admin.site.register(PostStatistic)
admin.site.register(Comment)