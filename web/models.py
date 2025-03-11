from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    date_time = models.DateTimeField(auto_now_add=True)
    # country = models.CharField(max_length=100, null=True, blank=True)
    # city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.ip_address} - {self.date_time}"