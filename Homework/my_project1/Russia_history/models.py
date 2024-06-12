from django.db import models


class History(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Russia_history/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

