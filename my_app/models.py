from django.db import models

# Create your models here.

class Blr_FanOnOffStatus(models.Model):
    status = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Blr_LightOnOffStatus(models.Model):
    status = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Vanc_FanOnOffStatus(models.Model):
    status = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Vanc_LightOnOffStatus(models.Model):
    status = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor1(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    timestamp = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

class Sensor2(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    timestamp = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

class Sensor3(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    timestamp = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

class Sensor4(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    timestamp = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

class Sensor5(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    timestamp = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

class Sensor6(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    timestamp = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
