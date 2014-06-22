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
    categories = models.ManyToManyField('Category', related_name="reviews")
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ["-pub_date"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(edit, kwargs={'pk': self.pk})

class Like(models.Model):
    user = models.ManyToManyField(User, related_name="likes")
    review = models.ForeignKey(Review)
    total_likes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse(edit, kwargs={'pk': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(edit, kwargs={'pk': self.pk})
