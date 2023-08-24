from django.contrib import admin

from apps.users.models import User

admin.site.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "phone_number",
#         "email",
#         "first_name",
#         "last_name",
#         "is_active",
#     )
#     ordering = ("-id",)
#     search_fields = ("phone_number", "email", "first_name", "last_name")
#     list_filter = ("is_active",)
#