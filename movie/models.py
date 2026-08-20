from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movie/images/')
    description = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
