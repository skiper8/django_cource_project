from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingDeleteView, MailingUpdateView, \
    MailingCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailings_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_form'),
]
