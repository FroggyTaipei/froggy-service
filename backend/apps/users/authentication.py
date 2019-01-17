import jwt

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

from rest_framework import exceptions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings


jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class AccountKitUserAuthentication(JSONWebTokenAuthentication):
    """
    """
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        """
        """
        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None

        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        user = self.authenticate_credentials(payload)

        return (user, jwt_value)

    def authenticate_credentials(self, payload):
        """
        """
        User = get_user_model()
        user_id = payload.get('id')

        if not user_id:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            msg = _('Invalid signature.')
            raise exceptions.AuthenticationFailed(msg)

        # if not user.is_active:
        #     msg = _('User account is disabled.')
        #     raise exceptions.AuthenticationFailed(msg)

        return user
