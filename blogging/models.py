from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Returns a string that identifies the model
        :return: String
        """

        return self.name

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    post = models.TextField()
    image = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    release_date = models.DateTimeField()
    category = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string that identifies the model
        :return: String
        """

        return self.title

    def clean(self):
        # Don't allow empty image or video.
        if (self.image == '' or self.image == None) and (self.url == '' or self.url == None):
            raise ValidationError(_('You must set and image or video.'))