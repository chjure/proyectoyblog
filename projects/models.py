from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    # image = models.FilePathField(path='/img/', null=True, blank=True)
    image = models.ImageField(upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return self.title