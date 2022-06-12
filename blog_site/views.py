from django.shortcuts import render
from blog.models import BlogPost

def home_view(request):
    obj = BlogPost.objects.all()
    template_name = "home.html"
    context = {
        'objects' : obj
    }
    return render(request,template_name,context)
