import firebase_admin
from firebase_admin import credentials, delete_app
from contextlib import contextmanager
from django.conf import settings


@contextmanager
def firebase_app(credential_path=settings.FIREBASE_SA_PATH):
    cred = credentials.Certificate(credential_path)
    app = firebase_admin.initialize_app(cred)
    try:
        yield app
    except Exception as e:
        raise e
    finally:
        delete_app(app)
