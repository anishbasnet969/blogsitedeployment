from django import forms

from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','slug','image','content','publish_date']