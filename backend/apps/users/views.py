import datetime
from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from firebase_admin import auth
from config.auth import firebase_app

from apps.users.models import User
from apps.users.utils import jwt_payload_handler, jwt_encode_handler
from apps.cases.models import TempFile


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    http_method_names = ['post']

    @action(methods=['POST'], detail=False, permission_classes=[])
    def token_auth(self, request):
        id_token = request.data.get('token')

        mobile = None

        with firebase_app() as app:
            try:
                decoded_token = auth.verify_id_token(id_token, app=app)
                uid = decoded_token['uid']
                user = auth.get_user(uid=uid, app=app)
                mobile = user.phone_number
            except (
                ValueError,
                auth.InvalidIdTokenError,
                auth.ExpiredIdTokenError,
                auth.UserNotFoundError
            ) as e:
                raise AuthenticationFailed(str(e))

        if not mobile.startswith('+886'):
            raise ValidationError('請使用國碼為 +886 的手機號碼進行驗證')

        mobile = mobile.replace('+886', '0')
        user = User.objects.filter(mobile=mobile).first()

        if not user:
            # Register a new user
            user = User.objects.create_auth0_user(email=None, mobile=mobile, full_name='Firebase User')

        temp_files = TempFile.objects.filter(user=user, upload_time__date=datetime.date.today())
        if temp_files.distinct('case_uuid').count() >= settings.FILE_LIMIT_CASE:
            raise ValidationError('您的手機號碼已超出每日服務次數限制，請聯絡本團隊為您處理')

        payload = jwt_payload_handler(user)
        jwt = jwt_encode_handler(payload)

        return JsonResponse({
            'jwt': jwt,
        })
