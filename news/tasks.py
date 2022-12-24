from krassite.celery import app
from news.service import send_mail_about_news


@app.task()
def send_spam(user_mail):
    send_mail_about_news(user_mail)
