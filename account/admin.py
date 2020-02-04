from django.contrib import admin

# Register your models here.

from .models import OTPUser,city,country,countrylanguage,Profile

admin.site.register(OTPUser)
admin.site.register(city)
admin.site.register(country)
admin.site.register(countrylanguage)
admin.site.register(Profile)

