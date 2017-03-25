from django.contrib import admin

# Register your models here.
from .models import Brother, Guest
admin.site.register(Brother)
admin.site.register(Guest)
