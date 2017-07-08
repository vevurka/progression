from django.db import models
from django.utils import timezone


class ClimbingWall(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ClimbingWallPlace(models.Model):
    climbing_wall = models.ForeignKey(to=ClimbingWall)
    place = models.CharField(max_length=10)

    def __unicode__(self):
        return str(self.climbing_wall) + " " + self.place

    def __str__(self):
        return str(self.climbing_wall) + " " + self.place


class Boulder(models.Model):
    color = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    place = models.ForeignKey(to=ClimbingWallPlace)

    def __unicode__(self):
        return  self.level + " " + self.place.place + " " + self.color

    def __str__(self):
        return self.level + " " + self.place.place + " " + self.color


class Tick(models.Model):
    boulder = models.ForeignKey(to=Boulder)
    tries = models.IntegerField()
    success = models.BooleanField()
    date = models.DateField(default=timezone.now)

    def __unicode__(self):
        return str(self.boulder) + " " + str(self.tries) + " " + str(self.date)