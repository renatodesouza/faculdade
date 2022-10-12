from tabnanny import verbose
from django.db import models




class Person(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Person'

    def __str__(self):
        return self.nome

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, related_name='groups')

    def __str__(self):
        return self.nome