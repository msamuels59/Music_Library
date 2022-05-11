from django.contrib import admin
from .models import Album, User

# Register your models here.

admin.site.register(User)
admin.site.register(Album)

