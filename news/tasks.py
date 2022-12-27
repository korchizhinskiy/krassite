from celery import shared_task
from news.service import send_mail_about_news


@shared_task(name="send_news")
def send_mail_task():
    send_mail_about_news()
