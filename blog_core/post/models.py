from django.db import models

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length = 100)
    content     = models.TextField()
    status      = models.CharField(max_length = 10, default = 'pending')
    tags        = models.TextField()
    author_id   = models.PositiveIntegerField()
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
