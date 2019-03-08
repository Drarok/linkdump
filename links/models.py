from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='links')
    url = models.CharField(max_length=2000, null=False, unique=True)
    title = models.CharField(max_length=2000, null=False, blank=True)
    selection = models.CharField(max_length=2000, null=False, blank=True)
    folder = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        ordering = ('-created', 'id')

    def __str__(self):
        return f'user_id={self.user_id}, url={self.url}'
