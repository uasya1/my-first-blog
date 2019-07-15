from django import forms

from .models import Post, Comment
from django.forms import ClearableFileInput

#class ImageField(**kwargs)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'video', 'image','text',  )#'video', 'image',


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


# class FileModelForm(forms.ModelForm):
#     class Meta:
#         model = PostFile
#         fields = ['file']
#         widgets = {
#             'file': ClearableFileInput(attrs={'multiple': True}),
#         }
#         # widget is important to upload multiple files
