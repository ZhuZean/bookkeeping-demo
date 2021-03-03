from django.contrib import admin
from user.models import UserProfile

# manage models on the admin site
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['nickname', 'mobile', 'gender']


admin.site.register(UserProfile, UserProfileAdmin)