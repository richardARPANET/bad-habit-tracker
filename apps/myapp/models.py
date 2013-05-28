from django.db import models
from django.contrib import admin


class Habit(models.Model):
    title = models.CharField(max_length=500)
    track_date = models.DateTimeField('data count started')
    pub_date = models.DateTimeField('date published')
    del_date = models.DateTimeField('data deleted', blank=True, null=True)
    ip_address = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

    def was_deleted(self):
        return self.del_date is not None

admin.site.register(Habit)