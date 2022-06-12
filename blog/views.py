from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import BlogPost
from .forms import BlogPostModelForm


# Create your views here.

#Blog-list
def blog_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = "blog/blog.html"
    context = {
        'objects' : qs
    }
    return render(request,template_name,context)

#CRUD Views
@login_required
def blog_create_view(request):
    form = BlogPostModelForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = "blog/form.html"
    context = {'form' : form}
    return render(request, template_name, context)


def blog_detail_view(request,slug):
    req_obj = get_object_or_404(BlogPost,slug=slug)
    template_name = "blog/detail.html"
    context = {
        'object' : req_obj
    }
    return render(request,template_name,context)

@login_required
def blog_update_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    form = BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    template_name = "blog/update.html"
    context = {
        'form' : form,
        "title": f"Update {obj.title}"
    }
    return render(request,template_name,context)

@login_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('home-page')
    template_name = "blog/delete.html"
    context = {
        "object":obj
    }
    return render(request,template_name,context)

