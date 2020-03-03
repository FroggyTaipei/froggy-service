import pickle
from django.core.management.base import BaseCommand
from django_redis import get_redis_connection

from apps.cases import insights


cache = get_redis_connection('default')


class Command(BaseCommand):

    def handle(self, **options):
        for data_func_name in insights.__all__:
            func = getattr(insights, data_func_name)
            data = pickle.dumps(func())
            cache.set(func.__name__, data)

        print('Insights data successfully cached!')
