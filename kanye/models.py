from django.db import models


class Quote(models.Model):
    name = models.CharField(max_length=255, unique=True)
    len_of_quote = models.IntegerField(null=False, blank=False)
    lower = models.IntegerField(null=False, blank=False)
    upper = models.IntegerField(null=False, blank=False)
    vowel = models.IntegerField(null=False, blank=False)
    consonants = models.IntegerField(null=False, blank=False)
