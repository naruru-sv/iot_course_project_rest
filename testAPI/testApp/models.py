from django.db import models
from datetime import datetime

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  title = models.CharField(max_length=120, primary_key=True, default=datetime.now)
  timestamp = models.DateTimeField(auto_now_add=True)
  size = models.CharField(max_length=100, blank=True)


