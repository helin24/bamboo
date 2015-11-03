from django.db import models

class ArrayGenerator(models.Model):
    size = models.IntegerField()
    generate_time = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)