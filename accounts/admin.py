from django.contrib import admin
from .models import Organization, User
# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
	list_display 		= ('name',)