from .celery import app
from django.core.mail import send_mail


@app.task
def send_email_task(user, code):
    full_link = f'http://35.203.116.125/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт.',
        f'Чтобы активировать аккаунт, вам необходимо перейти по ссылке: {full_link}',
        'kutmanvip01@gmail.com',
        [user],
        fail_silently=False,
    )
