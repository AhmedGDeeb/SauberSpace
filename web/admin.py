from django.contrib import admin
from .models import Visitor

from django.contrib.auth.models import User, Group
# Unregister the User and Group models
admin.site.unregister(User)
admin.site.unregister(Group)

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'date_time',)  # Columns to display in the admin list view
    search_fields = ('ip_address', 'date_time',)  # Add a search bar for specific fields
    list_filter = ('date_time',)  # Add filters for better navigation

    # Disable the "Add" button
    def has_add_permission(self, request):
        return False

    # Disable the "Delete" action
    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(Visitor, VisitorAdmin)

