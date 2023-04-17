from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class Note(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField(max_length=5000, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home', args=(str(self.pk)))

    def __str__(self):
        return f"{self.title} | {self.author} | {self.created}"
