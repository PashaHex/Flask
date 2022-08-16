from django.db import models

class Office(models.Model):
    addres = models.CharField(max_length=50)
    capacity = models.IntegerField()
    occupied = models.IntegerField()

class Request_donate(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    state = models.BooleanField(
        choices=((0, 'Available'), (1, 'Booked')), default=0
    )
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)

