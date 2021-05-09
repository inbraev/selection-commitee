from src.subdivision.models import Faculty, Direction, Section

form_education = (
    ('1', 'Очная'),
    ('2', 'Очная-заочная'),
    ('3', 'Заочная'),
    ('4', 'Экстернат')
)

education = (
    ('1', 'Бюджет'),
    ('2', 'Контракт'),
)


class FacultyService:
    model = Faculty

    @classmethod
    def filter(cls, **filters):
        return cls.model.objects.filter(**filters)


class DirectionService:
    model = Direction

    @classmethod
    def filter(cls, **filters):
        return cls.model.objects.filter(**filters)


class SectionService:
    model = Section

    @classmethod
    def filter(cls, **filters):
        return cls.model.objects.filter(**filters)
