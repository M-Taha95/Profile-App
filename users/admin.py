from django.contrib import admin
from .models import Users

admin.site.site_header = "Mohammed Taha"
admin.site.site_title = "Admin Area!"
admin.site.index_title = "Welcome to the profiler Admin"


class UserAdmin(admin.ModelAdmin):
    list_display = ["user_fname", "user_lname", "user_email", "user_position"]
    search_fields = ["user_fname", "user_lname", "user_email", "user_position"]

admin.site.register(Users, UserAdmin)
