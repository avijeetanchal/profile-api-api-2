from django.contrib import admin

from profiles_api import models

# Register your models here.
admin.site.register(models.UserProfile)
### this tell django admin to register this model with the admin site,,,
## so make this accessable to admin interface...

admin.site.register(models.ProfileFeedItem)
