from django.contrib import admin
from . models import User, StockUpSchedule

# Register your models here.
admin.site.register(User)
admin.site.register(StockUpSchedule)