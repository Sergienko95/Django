from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)


class Period(models.Model):
    month = models.CharField(max_length=50)
    year = models.IntegerField()


class Line(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)


class Form(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)


class Data(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    under_31 = models.IntegerField()
    over_31 = models.IntegerField()
