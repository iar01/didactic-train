from django.db import models
from apps.QLA.models import Subject


class Points(models.Model):
    Point = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Points'

    def __str__(self):
        return self.Point


class Bundle(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.FloatField()
    Discount = models.IntegerField(help_text='In Percentage')
    Annual_Discount = models.IntegerField(help_text='In Percentage')
    Annual_Price = models.IntegerField()
    Subjects = models.ManyToManyField(Subject)
    Point = models.ManyToManyField(to=Points)

    def save(self, *args, **kwargs):
        price_local = self.Price - (self.Price * self.Discount) / 100
        Annual_Price_local = (self.Price * 12) - (((self.Price * 12) * self.Annual_Discount) / 100)

        self.Price = price_local
        self.Annual_Price = Annual_Price_local

        super(Bundle, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Bundle offers'

    def __str__(self):
        return "{}-{}".format(self.Name, self.Price)
