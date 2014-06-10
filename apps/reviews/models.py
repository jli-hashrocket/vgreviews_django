from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200, blank=False)
    summary = models.TextField(blank=False)
    pros = models.TextField(blank=False)
    cons = models.TextField(blank=False)
    score = models.FloatField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(10)])
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ["-pub_date"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(edit, kwargs={'pk': self.pk})

