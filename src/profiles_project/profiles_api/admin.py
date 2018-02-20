from django.contrib import admin

from . import models

# register models here
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
