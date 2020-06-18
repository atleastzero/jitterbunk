from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photo_url = models.URLField()
    slug = models.SlugField(unique=True, default="Reset")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

class Bunk(models.Model):
    from_user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="from_user")
    to_user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="to_user")
    time_sent = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this bunk was sent.")

    def __str__(self):
        return (self.time_sent).strftime("%Y:%M:%D %H:%M:%S")
