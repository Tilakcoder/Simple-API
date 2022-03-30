from django.contrib import admin
from . models import Member, Parent, Children

# Register your models here.
admin.site.register(Member)
admin.site.register(Parent)
admin.site.register(Children)