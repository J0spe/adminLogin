from django.contrib import admin
from studentAccount.models import studentAccount
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class studentAccountInLine(admin.StackedInline):
    model = studentAccount
    can_delete = False
    verbose_name_plural = 'studentAccounts'

class customizedUser(UserAdmin):
    inlines = (studentAccountInLine, )

admin.site.unregister(User)
admin.site.register(User, customizedUser)