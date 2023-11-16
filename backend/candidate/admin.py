from django.contrib import admin
from .models import Candidate,Education,Referee
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Education)
admin.site.register(Referee)