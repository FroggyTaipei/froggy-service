from django.conf import settings
from google.oauth2 import service_account
from storages.backends.gcloud import GoogleCloudStorage


class CaseStorage(GoogleCloudStorage):
    project_id = settings.GS_PROJECT_ID
    credentials = service_account.Credentials.from_service_account_file(settings.DEFAULT_SA_PATH)
    bucket_name = settings.GS_CASE_BUCKET
    auto_create_bucket = True


class TempStorage(GoogleCloudStorage):
    project_id = settings.GS_PROJECT_ID
    credentials = service_account.Credentials.from_service_account_file(settings.DEFAULT_SA_PATH)
    bucket_name = settings.GS_TEMP_BUCKET
    auto_create_bucket = True
