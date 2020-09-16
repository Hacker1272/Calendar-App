from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    link = models.URLField()
    startdate = models.DateField()
    enddate = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.pk)+'-'+self.name

class Request(models.Model):
    status_choices = [
        ['APP','Approved'],
        ['PND','Pending'],
        ['RJD','Rejected']
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices = status_choices, default='PND')
    def __str__(self):
        return self.user.username+'-'+self.event.name

