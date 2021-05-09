from src.university.models import Student


class StudentService:
    model = Student

    @classmethod
    def filter(cls, **filters):
        return cls.model.objects.filter(**filters)
