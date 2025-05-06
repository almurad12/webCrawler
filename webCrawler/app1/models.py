from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
# Create your models here.
class CountryDetails(models.Model):
    name = JSONField(blank=True, null=True)
    tld = ArrayField(models.CharField(max_length=15), blank=True, default=list)
    cca2 = models.CharField(max_length=10, unique=True)
    ccn3 = models.CharField(max_length=10, blank=True, null=True)
    cioc = models.CharField(max_length=10, blank=True, null=True)
    independent = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    un_member = models.BooleanField(default=False)
    currencies = JSONField(blank=True, null=True)
    idd = JSONField(blank=True, null=True)
    capital = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    alt_spellings = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100)
    languages = JSONField(blank=True, null=True)
    latlng = ArrayField(models.FloatField(), blank=True, default=list)
    landlocked = models.BooleanField(default=False)
    borders = ArrayField(models.CharField(max_length=15), blank=True, default=list)
    area = models.FloatField() #
    demonyms = JSONField(blank=True, null=True)
    cca3 = models.CharField(max_length=15)
    translations = JSONField(blank=True, null=True)
    flag = models.CharField(max_length=15, blank=True, null=True)
    maps = JSONField(blank=True, null=True)
    population = models.BigIntegerField()
    gini = JSONField(blank=True, null=True)
    fifa = models.CharField(max_length=15, blank=True, null=True)
    car = JSONField(blank=True, null=True)
    timezones = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    continents = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    flags = JSONField(blank=True, null=True)
    coat_of_arms = JSONField(blank=True, null=True)
    start_of_week = models.CharField(max_length=15, blank=True, null=True)
    capital_info = JSONField(blank=True, null=True)
    postal_code = JSONField(blank=True, null=True)

    def __str__(self):
        return self.cca2
