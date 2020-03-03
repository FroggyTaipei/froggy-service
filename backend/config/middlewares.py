import logging

from django.http import HttpResponse, HttpResponseBadRequest
from django.conf import settings

logger = logging.getLogger("healthz")


class HealthCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.method == "GET":
            if request.path == "/readiness":
                return self.readiness(request)
            elif request.path == "/healthz":
                return self.healthz(request)
        return self.get_response(request)

    def healthz(self, request):
        """
        Returns that the server is alive.
        """
        return HttpResponse("OK")

    def readiness(self, request):
        # Connect to each database and do a generic standard SQL query
        # that doesn't write any data and doesn't depend on any tables
        # being present.
        try:
            from django.db import connections
            for name in connections:
                cursor = connections[name].cursor()
                cursor.execute("SELECT 1;")
                row = cursor.fetchone()
                if row is None:
                    return HttpResponseBadRequest("db: invalid response")
        except Exception as e:
            logger.exception(e)
            return HttpResponseBadRequest("db: cannot connect to database.")

        # Call get_stats() to connect to each memcached instance and get it's stats.
        # This can effectively check if each is online.
        try:
            from django_redis import get_redis_connection
            for key in settings.CACHES.keys():
                get_redis_connection(key)
        except Exception as e:
            logger.exception(e)
            return HttpResponseBadRequest("cache: cannot connect to cache.")

        return HttpResponse("OK")
