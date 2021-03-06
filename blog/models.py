from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    #text = models.TextField('texts')
    image = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    author = models.ForeignKey('auth.User')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
    	return self.comments.filter(approved_comment=True)

"""
class Electrical(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    author = models.ForeignKey('auth.User')

    def publish_electrical(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Electronics(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    author = models.ForeignKey('auth.User')

    def publish_electronics(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
"""



