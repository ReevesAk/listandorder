from django.contrib import admin
from . models import User, StockUpSchedule, SendMail

# Register your models here.
admin.site.register(User)
admin.site.register(StockUpSchedule)
admin.site.register(SendMail)
