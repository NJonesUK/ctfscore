from django.db import models
from django.contrib.auth.models import User
  
class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField()
    answer = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    def __unicode__(self):
        return self.title
            


class ChallengeEntry(models.Model):
    user = models.ForeignKey(User)
    challenge = models.ForeignKey(Challenge)

    class Meta:
        verbose_name = "Challenge Entry"
        verbose_name_plural = "Challenges Entries"

    def __unicode__(self):
        return str(self.user) + " : " + str(self.challenge)