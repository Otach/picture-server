from django.db import models

# Create your models here.
class Picture(models.Model):
    picture_id = models.UUIDField()
    picture_name = models.CharField(max_length=30)
    picture_description = models.TextField()

    def __str__(self):
        return f"{self.picture_name}: {self.picture_description}"

