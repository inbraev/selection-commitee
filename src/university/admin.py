from django.contrib import admin
from src.university.models import Student, AddressBirth, Parent, AddressParent, AddressLiving, AddressResidence, \
    EntryChallenge, OrtScoreInside


@admin.register(AddressParent)
class AddressParentInline(admin.ModelAdmin):
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


class ParentInline(admin.StackedInline):
    model = Parent
    fields_superuser = (
        'first_name', 'second_name', 'middle_name', 'job', 'position', 'phone', 'email', 'address', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('address',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


class AddressLivingInline(admin.StackedInline):
    model = AddressLiving
    fields_superuser = ('republic', 'region', 'district', 'city', 'village', 'phone', 'created_at')
    readonly_fields = ('created_at',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


class AddressResidenceInline(admin.StackedInline):
    model = AddressResidence
    fields_superuser = ('republic', 'region', 'district', 'city', 'village', 'phone', 'created_at')
    readonly_fields = ('created_at',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


class AddressBirthInline(admin.StackedInline):
    model = AddressBirth
    fields_superuser = ('republic', 'region', 'district', 'city', 'village', 'created_at')
    readonly_fields = ('created_at',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(OrtScoreInside)
class OrtScoreInsideAdmin(admin.ModelAdmin):
    fields_superuser = (
        'basic_score', 'bio_sub_score', 'phy_sub_score', 'chem_sub_score', 'math_sub_score',
        'his_sub_score', 'eng_sub_score', 'created_at')
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


class EntryChallengeInline(admin.StackedInline):
    model = EntryChallenge
    fields_superuser = (
        'qualifying_round_number', 'passed_ort', 'certificate_num', 'certificate_color', 'ort', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('ort',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'second_name', 'middle_name', 'avatar', 'phone', 'sex', 'dob', 'created_at')
    list_display = ('first_name', 'second_name', 'middle_name', 'phone', 'sex', 'dob', 'created_at')
    search_fields = ('first_name', 'second_name', 'middle_name',)
    list_filter = ('sex',)
    readonly_fields = ('created_at',)
    inlines = [AddressBirthInline, AddressLivingInline, AddressResidenceInline, ParentInline, EntryChallengeInline]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display