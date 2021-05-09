from django.contrib import admin
from src.university.models import Student, AddressBirth,


class AddressBirthInline(admin.StackedInline):
    model = AddressBirth
    fields_superuser = ('republic', 'region', 'district', 'city', 'village', 'created_at')
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


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'second_name', 'middle_name', 'avatar', 'phone', 'sex', 'dob', 'created_at')
    list_display = ('first_name', 'second_name', 'middle_name', 'phone', 'sex', 'dob', 'created_at')
    search_fields = ('first_name', 'second_name', 'middle_name',)
    list_filter = ('sex',)
    readonly_fields = ('created_at',)
    inlines = [AddressBirthInline]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display
