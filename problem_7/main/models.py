from django.db import models

# Create your models here.


class Salary(models.Model):
    salary = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Salary'

    def __str__(self):
        return str(self.salary)


class Work(models.Model):
    work = models.CharField(max_length=150)
    salary = models.ForeignKey(
        Salary, default=1, verbose_name='Salary', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = 'Work'

    def __str__(self):
        return self.work


class Name(models.Model):
    name = models.CharField(max_length=150)
    work = models.ForeignKey(
        Work, default=1, verbose_name='Work', on_delete=models.SET_DEFAULT)
    salary = models.ForeignKey(
        Salary, default=1, verbose_name='Salary', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = 'Name'

    def __str__(self):
        return self.name
