from django.http import JsonResponse
from django.middleware import csrf


def get_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'token': token})
