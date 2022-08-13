from django.contrib import admin
from.models import User
from.models import Book_ground,Admin,Event

# Register your models here.
admin.site.register(User)
admin.site.register(Book_ground)
admin.site.register(Admin)
admin.site.register(Event)


