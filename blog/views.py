from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.forms import BlogForms
from blog.models import Blog, Contacts


class BlogListView(ListView):
    model = Blog
    form_class = BlogForms

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    form_class = BlogForms

    def get_object(self, queryset=None):
        object = super().get_object(queryset=queryset)
        object.view_count += 1
        object.save()
        return object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'text', 'image', 'is_active')
    success_url = reverse_lazy('mailing:blog_list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'text', 'image', 'is_active')

    def get_success_url(self):
        return reverse('mailing:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('mailing:blog_list')


class ContactView(TemplateView):
    """Представление страницы контактов сервиса"""
    model = Contacts
