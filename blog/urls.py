from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, ContactView

urlpatterns = [
    path('contacts/', ContactView.as_view(template_name='blog/contacts.html'), name='contacts'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/<str:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<str:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
