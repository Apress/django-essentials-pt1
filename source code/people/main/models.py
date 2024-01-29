from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

