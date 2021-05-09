from django.contrib import admin
from src.recruitmentplan.models import Plan, OrtScore
from src.subdivision.services import DirectionService


class OrtScoreInline(admin.TabularInline):
    model = OrtScore
    fields_superuser = (
        'basic_score', 'kyr_sub_score', 'bio_sub_score', 'phy_sub_score', 'chem_sub_score', 'math_sub_score',
        'his_sub_score', 'eng_sub_score', 'rus_sub_score', 'created_at')
    readonly_fields = ('created_at',)
    extra = 1

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    fields_superuser = (
        'faculty', 'direction', 'section', 'form_education', 'education', 'additional_item', 'planned_place',
        'doc_money', 'study_money', 'req_additional_subject', 'created_at')
    list_filter = ('faculty', 'direction', 'section', 'form_education', 'education',)
    raw_id_fields = ('faculty', 'direction', 'section')
    readonly_fields = ('created_at',)
    inlines = (OrtScoreInline,)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display(self, request):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser and request.user.is_staff:
            return self.fields_superuser
