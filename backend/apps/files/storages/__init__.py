from django.conf import settings


if settings.USE_GCS:
    from .gcloud import CaseStorage, TempStorage

else:
    from .local import CaseStorage, TempStorage


__all__ = (
    CaseStorage,
    TempStorage,
)
