from src.user.models import PermissionCommissioner


class PermissionCommissionerService:
    model = PermissionCommissioner

    @classmethod
    def filter(cls, **filters):
        return cls.model.objects.filter(**filters)
