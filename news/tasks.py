from celery import shared_task
from news.service import send_mail_about_news


@shared_task
def send_mail_task():
    send_mail_about_news(["nosafeyou@mail.ru"])
