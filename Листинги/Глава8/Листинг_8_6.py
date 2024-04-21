from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="Имя клиента")
    age = models.IntegerField(verbose_name="Возраст клиента")
    object_person = models.Manager()
    DoesNotExist = models.Manager
