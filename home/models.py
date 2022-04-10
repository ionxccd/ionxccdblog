from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="img_sources/%y")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.TextField(editable=False)
    def __str__(self):
        return self.title
# Create your models here.
