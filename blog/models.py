from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

#
# class PostFile(models.Model):
#     file = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True, help_text='Only webm or mp4', verbose_name='video',)
#     #feed = models.ForeignKey(Post, on_delete=models.CASCADE)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #files = models.ManyToManyField(PostFile)
    video = models.FileField(upload_to='media/%Y/%m/%d/',null=True, blank=True, help_text='Only webm or mp4', verbose_name='video',)
    image = models.ImageField(upload_to='image/%Y/%m/%d/',null=True, blank=True, )
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


