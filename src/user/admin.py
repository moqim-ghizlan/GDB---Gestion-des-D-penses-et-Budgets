from django.contrib import admin
from .models import User




class UserAdminConfig(admin.ModelAdmin):
    list_display = ('get_last_name', 'get_first_name', 'get_email', 'is_admin')
    list_display_links = ('get_last_name', 'get_first_name', 'get_email', 'is_admin')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


    def is_admin(self, obj):
        return obj.is_superuser
    is_admin.boolean = True
    is_admin.short_description = 'Admin'

    def get_last_name(self, obj):
        return obj.get_last_name()

    def get_first_name(self, obj):
        return obj.get_first_name()

    def get_email(self, obj):
        return obj.email



    get_last_name.short_description = 'Last name'
    get_first_name.short_description = 'First name'
    get_email.short_description = 'Email'

admin.site.register(User, UserAdminConfig)
