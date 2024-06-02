from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='video/images/', default='video/images/default.jpg')

    def __str__(self):
        return self.name