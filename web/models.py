from django.db import models

from .utils import valid_date, valid_hour

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    date_time = models.DateTimeField(auto_now_add=True)
    # country = models.CharField(max_length=100, null=True, blank=True)
    # city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.ip_address} - {self.date_time}"
    

class Visits(models.Model):
    date = models.DateField(auto_now_add=False)
    hour = models.TimeField(auto_now_add=False)

    def clean(self):
        day_is_valid, _ = valid_date(self.date)
        if not day_is_valid:
            raise ValueError('day: {} is not valid'.format(self.date))
        hour_is_valid, max_valid_hour, min_valid_hour = valid_hour(self.hour)
        if not hour_is_valid:
            raise ValueError('hour must be in the valid range [{}, {}]'.format(max_valid_hour, min_valid_hour))

        super().clean()

    def __str__(self):
        return f"{self.date} - {self.hour}"