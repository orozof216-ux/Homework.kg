from django.contrib import admin
from .models import Person, Horse, TourCompany, Service, Review

admin.site.register(Person)
admin.site.register(Horse)
admin.site.register(TourCompany)
admin.site.register(Service)
admin.site.register(Review)
