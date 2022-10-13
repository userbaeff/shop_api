from django.core.mail import send_mail


def send_confirmation_mail(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте Ваш аккаунт',
        f'Чтобы активировать Ваш аккаунт нужно перйти по ссылке ниже: \n{full_link}',
        'usermaks47@gmail.com',
        [user],
        fail_silently=False)

