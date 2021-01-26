from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display=('id','firstname','lastname','profilepic','email','phone','room','subjects')