from django.conf import settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class IPMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip_address = request.META.get('HTTP_REMOTE_ADDR')

        if ip_address in ['127.0.0.1', 'localhost']:
            ip_address = getattr(settings, 'RT_IP_LOCALHOST', '127.0.0.1')
        else:
            ip_address = getattr(settings, 'RT_IP_SUBSTITUTES', {}).get(ip_address, ip_address)

        request.ip_address = ip_address
