from django.db import models
from taggit.managers import TaggableManager


class Footwear(models.Model):
    name = models.CharField(max_length=225)
    image_url = models.CharField(max_length=2083)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Top(models.Model):
    name = models.CharField(max_length=225)
    image_url = models.CharField(max_length=2083)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Bottom(models.Model):
    name = models.CharField(max_length=225)
    image_url = models.CharField(max_length=2083)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Accessorie(models.Model):
    name = models.CharField(max_length=225)
    image_url = models.CharField(max_length=2083)
    tags = TaggableManager()

    def __str__(self):
        return self.name
