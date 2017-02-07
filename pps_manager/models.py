from django.db import models

# Create your models here.

class BlacklistEntry(models.Model):
    BlacklistKey = models.CharField(max_length = 255, db_index = True)

    def __str__(self):
        return self.BlacklistKey

class WhitelistEntry(models.Model):
    WhitelistEntry = models.CharField(max_length = 255, db_index = True)

    def __str__(self):
        return self.WhitelistKey
