from django.db import models


class Ad(models.Model):
    url = models.CharField()
    dept_code = models.CharField(null=True)
    zip_code = models.IntegerField(null=True)
    city = models.CharField()
    annual_condominium_fees = models.IntegerField(null=True)

    def __str__(self):
        return self.url
