from django.contrib import admin
from .models import Service, Review, RequestContact, UserReview, Invoice, BlogPost

# Register your models here.
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(RequestContact)
admin.site.register(UserReview)
admin.site.register(Invoice)
admin.site.register(BlogPost)

