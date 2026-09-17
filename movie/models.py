from django.db import models
import numpy as np


def get_default_array():
    default_arr = np.random.rand(1536).astype(np.float32)
    return default_arr.tobytes()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movie/images/')
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    genre = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(blank=True, null=True)
    emb = models.BinaryField(default=get_default_array)

    def __str__(self):
        return self.title
