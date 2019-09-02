from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Instructor(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    rank = models.CharField(max_length=100, default = "")
    image = models.ImageField(default='default.jpg', upload_to='instructor_pics')
    text = HTMLField()
    page_order = models.IntegerField(default = 0)
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    
class Officer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='officer_pics')
    text = HTMLField()
    page_order = models.IntegerField(default = 0)
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    
class Alumni(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    classyear = models.IntegerField(default = 0)
    course = models.IntegerField(default = 0)
    image = models.ImageField(default='default.jpg', upload_to='alumni_pics')
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    
class FAQ(models.Model):
    ID = models.AutoField(primary_key=True)
    text = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    
class Practices(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    days = models.CharField(max_length=100, default = "")
    time = models.CharField(max_length=100, default = "")
    location = models.CharField(max_length=100, default = "")
    icon = models.CharField(max_length=100, default = "flaticon-martial-arts")
    description = HTMLField()
    page_order = models.IntegerField(default = 0)
    
class Tournaments(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    LeagueType = models.CharField(max_length=100, default = "ECTC")
    timing = models.CharField(max_length=100, default = "")
    icon = models.CharField(max_length=100, default = "flaticon-martial-arts")
    description = HTMLField()
    page_order = models.IntegerField(default = 0)
    semester = models.CharField(max_length=100, default = "Fall")

class majorfriend(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    friendtype = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='friend_pics')
    contribution = models.CharField(max_length=100, default="0")
    text = HTMLField()
    date_contributed = models.DateTimeField(default=timezone.now)
    last_contributed = models.DateTimeField(auto_now=True)
    page_order = models.IntegerField(default=5000)
    active = models.BooleanField(default=True)

class minorfriend(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    contribution = models.CharField(max_length=100)
    date_contributed = models.DateTimeField(default=timezone.now)
    last_contributed = models.DateTimeField(auto_now=True)
    page_order = models.IntegerField(default=5000)
    active = models.BooleanField(default=True)