from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from src.user.models import Users, Commissioner, PermissionCommissioner

admin.site.site_header = "Приемная комиссия"
admin.site.site_title = "Приемная комиссия"
admin.site.index_title = "Приемная комиссия"


class CommissionerInline(admin.StackedInline):
    model = Commissioner
    fields_superuser = (
        'first_name', 'second_name', 'middle_name', 'user', 'phone', 'whats_app', 'telegram', 'instagram', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('user',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(Commissioner)
class CommissionerAdmin(admin.ModelAdmin):
    fields_superuser = (
        'first_name', 'second_name', 'middle_name', 'user', 'phone', 'whats_app', 'telegram', 'instagram', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('user',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(PermissionCommissioner)
class PermissionCommissionerAdmin(admin.ModelAdmin):
    fields_superuser = ('commissioner', 'education', 'faculty', 'created_at')
    raw_id_fields = ('commissioner', 'faculty',)
    readonly_fields = ('created_at',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(Users)
class UsersAdmin(UserAdmin):
    model = Users
    list_display = (
        'id', 'email', 'is_staff', 'is_superuser', 'is_active', 'created_at')
    list_display_links = (
        'id', 'email', 'is_staff', 'is_superuser', 'is_active', 'created_at')
    fieldsets = (
        (None, {'fields': (
            'email', 'is_active', 'is_staff', 'created_at',)
        }),
    )
    ordering = ('email',)
    list_filter = ('email', 'is_active')
    search_fields = ('email',)
    inlines = (CommissionerInline,)
    readonly_fields = ('created_at',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2'
            )}
         ),
    )

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return True

    def has_add_permission(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return True

    def has_module_permission(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return True


admin.site.unregister(Group)
