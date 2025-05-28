from django.contrib import admin
from .models import Task


ALLOWED_USERNAMES = ['foo@company.com', 'bar@gmail.com', 'pradana']

@admin.action(description='Mark selected tasks as completed')
def mark_completed(modeladmin, request, queryset):
    queryset.update(is_completed=True)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title',)
    list_editable = ('is_completed',)  # 👈 FIXED: see below
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    actions = [mark_completed]

    def short_description(self, obj):
        if obj.description:
            return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
        return '-'
    short_description.short_description = 'Description'

    # def has_module_permission(self, request):
    #     return request.user.is_superuser

    # def has_view_permission(self, request, obj=None):
    #     return request.user.is_superuser

    # def has_add_permission(self, request):
    #     return request.user.is_superuser

    # def has_change_permission(self, request, obj=None):
    #     return request.user.is_superuser

    # def has_delete_permission(self, request, obj=None):
    #     return request.user.is_superuser

    def has_module_permission(self, request):
        return request.user.get_username() in ALLOWED_USERNAMES

    def has_view_permission(self, request, obj=None):
        return request.user.get_username() in ALLOWED_USERNAMES

    def has_add_permission(self, request):
        return request.user.get_username() in ALLOWED_USERNAMES

    def has_change_permission(self, request, obj=None):
        return request.user.get_username() in ALLOWED_USERNAMES

    def has_delete_permission(self, request, obj=None):
        return request.user.get_username() in ALLOWED_USERNAMES