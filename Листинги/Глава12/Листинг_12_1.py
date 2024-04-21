# Чтение SECRET_KEY из переменной окружения
import os
SECRET_KEY = os.environ['SECRET_KEY']
# ИЛИ чтение ключа из файла
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
