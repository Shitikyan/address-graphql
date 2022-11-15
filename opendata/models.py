from django.db import models


# Create your models here.
class NYCBuilding(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    building_city = models.CharField(max_length=255, default='NYC')
    state = models.CharField(max_length=255, default='NY')
    gross_sqft = models.CharField(max_length=255, default='-')
    yrbuilt = models.IntegerField(default=-1)
    pytaxclass = models.CharField(max_length=255, default='-')
    owner = models.CharField(max_length=255, default='-')

    class Meta:
        verbose_name_plural = 'NYC buildings'

    def __str__(self):
        return self.address

