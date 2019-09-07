from django.contrib import admin
from .models import Instructor, Officer, Alumni, FAQ, Practices, Tournaments, majorfriend, minorfriend

admin.site.register(Instructor)
admin.site.register(Officer)
admin.site.register(Alumni)
admin.site.register(FAQ)
admin.site.register(Practices)
admin.site.register(Tournaments)
admin.site.register(majorfriend)
admin.site.register(minorfriend)