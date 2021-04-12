from django.db import models

class Users(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)

    name = models.CharField(default="", max_length=200)
    phoneno = models.CharField(default="", max_length=13)
    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Users, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self._id)

    class Meta:
        db_table = 'users'
        app_label = 'src'
