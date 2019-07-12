from django import forms

from .models import Post, Comment

#class ImageField(**kwargs)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'document', 'image', 'text', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)



