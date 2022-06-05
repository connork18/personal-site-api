from django.db import models

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
    )

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    published_on = models.DateTimeField()
    content = models.TextField()
    created_on = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

TYPE = (
    (0, "Yoga"),
    (1, "Conditioning"),
    (2, "Upper"),
    (3, "Lower"),
    (4, "Full"),
    (5, "Recovery"),
    )

class Workout(models.Model):
    date = models.DateTimeField()
    content = models.TextField()
    type = models.IntegerField(choices=TYPE)

    class Meta:
        ordering = ['-date']