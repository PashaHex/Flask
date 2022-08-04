from django.db import models


class Request_donate(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    state = models.BooleanField(
        choices=((0, 'Free'), (1, 'Booked')), default=0
    )

