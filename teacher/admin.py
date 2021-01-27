from django.contrib import admin

# Register your models here.
from .models import User
from import_export.admin import ImportExportModelAdmin
 


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
	list_display=('id','firstname','lastname','profilepic','email','phone','room','subjects')