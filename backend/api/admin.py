from django.contrib import admin

from api.models import Wine, Review

# Register your models here.
admin.site.register(Wine)
admin.site.register(Review)