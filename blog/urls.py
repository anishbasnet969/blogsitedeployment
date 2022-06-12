from django.urls import path, include
from .views import (
                    blog_detail_view,
                    blog_list_view,
                    blog_create_view,
                    blog_post_delete_view,
                    blog_update_view
                    )


urlpatterns = [
    path('', blog_list_view),
    path('create/', blog_create_view),
    path('<str:slug>/', blog_detail_view),
    path('<str:slug>/delete', blog_post_delete_view),
    path('<str:slug>/edit', blog_update_view),
]