from django.db import models
from organiser.models import Startup, Tag
import datetime

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text='A label for URL config.',
        unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(default=datetime.date.today)
    startups = models.ManyToManyField(Startup)

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date', 'title']
        verbose_name = "blog post"

    def __str__(self):
        date_str = self.pub_date.strftime('%Y-%m-%d')
        return f"{date_str}: {self.title}"