# library_app/models.py

from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100, null=True, blank=True)
    datecreate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname
