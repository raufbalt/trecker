from django.core.mail import send_mail


def send_code_password_reset(user):
    code = user.activation_code
    email = user.email
    send_mail(
        'Письмо с кодом для сброса пароля!',
        f'Ваш код для того чтобы восстановить пароль: {code}\nНикому не передавайте этот код!',
        'kutmanvip01@gmail.com',
        [email],
        fail_silently=False
    )