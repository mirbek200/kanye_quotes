from django.db import models


class Quote(models.Model):
    name = models.CharField(max_length=255)
