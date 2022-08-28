from django.db import models

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Coupon Code'

    def __str__(self):
        return self.code
