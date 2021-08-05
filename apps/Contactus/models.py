from django.db import models


# Create your models here.
class Contactus(models.Model):
    Email = models.EmailField()
    Phone = models.CharField(max_length=100)
    Facebook = models.URLField(max_length=100)
    Twitter = models.URLField(max_length=100)
    Address = models.TextField()

    def __str__(self):
        return str(self.Email)

    class Meta:
        verbose_name_plural = 'Contactus'
