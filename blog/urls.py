from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, ContactView

app_name = BlogConfig.name

urlpatterns = [
    path('contacts/', ContactView.as_view(template_name='blog/contact.html'), name='contacts'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/update/<str:slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<str:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]
