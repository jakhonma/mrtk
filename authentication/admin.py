from django.contrib import admin
from authentication.models import User, AdminUser, LeaderUser, EmployeeUser, LowUser

admin.site.register([User, AdminUser, LeaderUser, EmployeeUser, LowUser])
