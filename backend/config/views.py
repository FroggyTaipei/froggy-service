import environ

from django.http import JsonResponse
from django.core.signing import TimestampSigner


env = environ.Env()


ACCOUNTKIT_APP_ID = env.str('VUE_APP_ACCOUNTKIT_APP_ID')


def get_token(request):
    signer = TimestampSigner()
    state = signer.sign(ACCOUNTKIT_APP_ID)
    return JsonResponse({
        'state': state,
    })
