# настройки отправки e-mail
''' это пробная отправка на консоль '''
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

''' это реальная отправка через smtp.gmail '''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True  # для отправки с gmail
EMAIL_PORT = 465
EMAIL_HOST_USER = "my_address@gmail.com"  # от кого
EMAIL_HOST_PASSWORD = "ftcsfgtjktuitpia"  # пароль почты отправителя
