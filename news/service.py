from django.core.mail import send_mail
from krassite import settings


def send_mail_about_news(user_mail: list[str]):
    send_mail(
        'Вы подписались на рассылку',
        'Мы пришлем еще сообщения',
        settings.EMAIL_HOST_USER,
        recipient_list=user_mail,
    )
