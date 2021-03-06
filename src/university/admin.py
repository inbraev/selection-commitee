from django.contrib import admin

from src.university.models import Student, AddressBirth, EducationName, EducationType, Passport, Percs, Education, \
    EducationPlace, MilitaryService, EnrollmentData, Parent, AddressParent, AddressLiving, AddressResidence, \
    EntryChallenge, OrtScoreInside

from src.user.services import PermissionCommissionerService
from src.university.services import StudentService
from src.subdivision.services import education


class PercsInline(admin.StackedInline):
    model = Percs
    fields_superuser = ('orphan', 'invalid', 'ethnical_kyrgyz', 'care', 'created_at')
    readonly_fields = ('created_at',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(AddressParent)
class AddressParentAdmin(admin.ModelAdmin):
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


class PassportInline(admin.StackedInline):
    model = Passport
    fields_superuser = (
        'inn', 'serial_number', 'family_status', 'citizenship', 'get_date', 'issuing_auth', 'created_at')
    readonly_fields = ('created_at',)


class EntryChallengeInline(admin.StackedInline):
    model = EntryChallenge
    fields_superuser = (
        'qualifying_round_number', 'passed_ort', 'certificate_num', 'certificate_color', 'ort', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('ort',)

    def get_fields(self, request, obj=None):
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


@admin.register(EducationType)
class EducationTypeAdmin(admin.ModelAdmin):
    fields_superuser = ('name', 'created_at')
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


@admin.register(EducationName)
class EducationNameAdmin(admin.ModelAdmin):
    fields_superuser = ('name', 'created_at')
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


@admin.register(EducationPlace)
class EducationPlaceAdmin(admin.ModelAdmin):
    model = EducationPlace
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


class EducationInline(admin.StackedInline):
    model = Education
    fields_superuser = ('original_diploma', 'excellent_student', 'gold_medal', 'prize_winner', 'diploma_or_certificate',
                        'serial_diploma_or_certificate',
                        'num_diploma_or_certificate', 'year_of_issue', 'school_language', 'foreign_language',
                        'out_of_competition',
                        'kstu_student', 'sport_name', 'sport_document_number', 'education_place', 'type_of_education',
                        'education_name', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('education_place', 'type_of_education', 'education_name')

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


class EnrollmentInline(admin.StackedInline):
    model = EnrollmentData
    fields_superuser = ('day_form', 'language_rus', 'study_form', 'direction', 'recommended', 'protocol',
                        'recommended_date', 'paid', 'confirm_enrollment', 'confirm_date',
                        'enrollment', 'order_num', 'order_date', 'protocol_num', 'protocol_date',
                        'took_docs', 'took_docs_date', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('direction',)

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

    inlines = [AddressBirthInline, AddressLivingInline, AddressResidenceInline, ParentInline, EntryChallengeInline,
               PassportInline, EducationInline, EnrollmentInline, MilitaryServiceInline, PercsInline]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields
        elif request.user.is_staff:
            return self.fields

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display
        elif request.user.is_staff:
            return self.list_display

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.list_display
        elif request.user.is_staff:
            return self.list_display

    def has_add_permission(self, request):
        return True

    def has_module_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    # def get_queryset(self, request):
    #     qs = super(StudentAdmin, self).get_queryset(request)
    #     if request.user.is_superuser and request.user.is_staff:
    #         return qs
    #     elif request.user.is_staff:
    #         perm_staff = PermissionCommissionerService.filter(commissioner__user=request.user)
    #         e1 = set(perm_st.education for perm_st in perm_staff)
    #         e2 = list(set(perm_st.faculty for perm_st in perm_staff))
    #         return qs.filter(enroll_student__study_form__in=e1, enroll_student__direction__faculty__in=e2)
