from django.core.mail import send_mail
from krassite import settings
from news.models import Contact
from constance import config


def send_mail_about_news():
    send_mail(
        config.MESSAGE_TOPIC,
        config.MESSAGE_TEXT,
        settings.DEFAULT_FROM_EMAIL,
        get_contacts_for_send_mail(),
        fail_silently=False
    )


def get_contacts_for_send_mail() -> list[str]:
    queryset = Contact.objects.all()
    emails = [contact.email for contact in queryset]
    return emails
