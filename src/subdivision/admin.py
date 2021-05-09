from django.contrib import admin

from src.subdivision.models import Vuz, Faculty, Direction, Section


@admin.register(Vuz)
class VuzAdmin(admin.ModelAdmin):
    fields_superuser = ('name', 'short_name', 'address', 'created_at')
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


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    fields_superuser = ('name', 'short_name', 'vuz', 'created_at')
    search_fields = ('name', 'short_name')
    readonly_fields = ('created_at',)
    raw_id_fields = ('vuz',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    fields_superuser = ('cipher', 'name', 'faculty', 'created_at')
    search_fields = ('name', 'cipher')
    list_filter = ('faculty',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('faculty',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    fields_superuser = ('name', 'direction', 'created_at')
    search_fields = ('name',)
    list_filter = ('direction',)
    preserve_filters = ('name',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('direction',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser
