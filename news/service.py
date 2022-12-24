from django.core.mail import send_mail


def send_mail_about_news(user_mail):
    send_mail(
        'Вы подписались на рассылку',
        'Мы пришлем еще сообщения',
        'nosafeyou@mail.ru',
        [user_mail],
        fail_silently=False
    )
