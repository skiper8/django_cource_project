from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingForms
from mailing.models import Mailing


class MailingListView(LoginRequiredMixin, ListView):
    """Представление для просмотра рассылок"""
    model = Mailing
    extra_context = {'title': 'Рассылки'}

    def get_queryset(self):
        """Функция, позволяющая просматривать только свои рассылки для пользователя, который не является менеджером"""
        user = self.request.user
        if user.is_superuser or user.is_staff:
            queryset = Mailing.objects.all()
        else:
            queryset = Mailing.objects.filter(user=user)

        queryset = queryset.filter(is_published=True)
        return queryset


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    form_class = MailingForms


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = ('mail_title', 'mail_text', 'mail_time', 'status', 'users_email', 'period',)
    success_url = reverse_lazy('mailing:mailing_list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ('mail_title', 'mail_text', 'period', 'status', 'users_email', 'mail_time')

    def get_success_url(self):
        return reverse('mailing:mailing_detail', kwargs={'pk': self.object.pk})


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
