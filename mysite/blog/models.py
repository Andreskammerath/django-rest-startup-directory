from django.db import models
from organiser.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    text = models.TextField()
    pub_date = models.DateField()
    startups = models.ManyToManyField(Startup)