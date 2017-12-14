from django.conf import settings


RT_IP_LOCALHOST = getattr(settings, 'RT_IP_LOCALHOST', '127.0.0.1')
RT_IP_SUBSTITUTES = getattr(settings, 'RT_IP_SUBSTITUTES', {})
RT_IP_SUBSTITUTES['127.0.0.1'] = RT_IP_LOCALHOST
RT_IP_SUBSTITUTES['localhost'] = RT_IP_LOCALHOST
