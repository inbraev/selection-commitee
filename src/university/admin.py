from django.contrib import admin
from src.university.models import Student, AddressBirth, EducationName, EducationType, Passport, Percs, Education, \
    EducationPlace, MilitaryService, EnrollmentData


class PercsInline(admin.StackedInline):
    model = Percs
    fields_superuser = ('orphan', 'invalid', 'ethnical_kyrgyz', 'care', 'created_at')
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


class PassportInline(admin.StackedInline):
    model = Passport
    fields_superuser = (
        'inn', 'serial_number', 'family_status', 'citizenship', 'get_date', 'issuing_auth', 'created_at')
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


class MilitaryServiceInline(admin.StackedInline):
    model = MilitaryService
    fields_superuser = ('document', 'serial_number', 'name_of_military_regis', 'military_registration_date', 'good',
                        'special_account', 'special_account_number', 'transferred_to_the_reserve', 'rank',
                        'military_registration_speciality',
                        'military_registration_number',
                        'created_at')
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


class EducationTypeInline(admin.StackedInline):
    model = EducationType
    fields_superuser = ('name', 'type_of_education' 'created_at')
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


class EducationNameInline(admin.StackedInline):
    model = EducationName
    fields_superuser = ('name', 'education_name', 'created_at')
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


class EducationPlaceInline(admin.StackedInline):
    model = EducationPlace
    fields_superuser = ('republic', 'region', 'district', 'city', 'village', 'created_at')
    readonly_fields = ('created_at',)
    inlines = [EducationTypeInline, EducationNameInline]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


class EducationInline(admin.StackedInline):
    model = Education
    fields_superuser = ('original_diploma', 'excellent_student', 'gold_medal', 'prize_winner', 'diploma_or_certificate',
                        'serial_diploma_or_certificate',
                        'num_diploma_or_certificate', 'year_of_issue', 'school_language', 'foreign_language',
                        'out_of_competition',
                        'kstu_student', 'sport_name', 'sport_document_number',
                        'created_at')
    readonly_fields = ('created_at',)
    inlines = [EducationPlaceInline]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


class EnrollmentInline(admin.StackedInline):
    model = EnrollmentData
    fields_superuser = ('day_form', 'language_rus', 'study_form', 'recommended', 'protocol',
                        'recommended_date',
                        'paid', 'confirm_enrollment', 'confirm_date', 'enrollment',
                        'order_num',
                        'order_date', 'protocol_num', 'protocol_date', 'took_docs', 'took_docs_date'
                                                                                    'created_at')
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
    inlines = [AddressBirthInline, PassportInline, EducationInline,EnrollmentInline, MilitaryServiceInline, PercsInline]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display
