from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photo_url = models.URLField()

class Bunk(models.Model):
    from_user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="from_user")
    to_user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="to_user")
    time_sent = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this bunk was sent.")

