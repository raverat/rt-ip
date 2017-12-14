from django.test import TestCase, RequestFactory, override_settings


class GeoIPMiddlewareTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_ip(self):
        from rt_ip.middleware import IPMiddleware

        request = self.factory.get('/', HTTP_REMOTE_ADDR='187.34.29.3')

        middleware = IPMiddleware()
        self.assertIsNone(middleware.process_request(request))
        self.assertEqual(getattr(request, 'ip_address', None), '187.34.29.3')

    def test_localhost(self):
        from rt_ip.middleware import IPMiddleware

        request = self.factory.get('/', HTTP_REMOTE_ADDR='127.0.0.1')

        middleware = IPMiddleware()
        self.assertIsNone(middleware.process_request(request))
        self.assertEqual(getattr(request, 'ip_address', None), '127.0.0.1')

        request = self.factory.get('/', HTTP_REMOTE_ADDR='localhost')

        middleware = IPMiddleware()
        self.assertIsNone(middleware.process_request(request))
        self.assertEqual(getattr(request, 'ip_address', None), '127.0.0.1')

    @override_settings(RT_IP_LOCALHOST='98.43.23.2')
    def test_replace_localhost(self):
        from rt_ip.middleware import IPMiddleware

        request = self.factory.get('/', HTTP_REMOTE_ADDR='127.0.0.1')

        middleware = IPMiddleware()
        self.assertIsNone(middleware.process_request(request))
        self.assertEqual(getattr(request, 'ip_address', None), '98.43.23.2')

        request = self.factory.get('/', HTTP_REMOTE_ADDR='localhost')

        middleware = IPMiddleware()
        self.assertIsNone(middleware.process_request(request))
        self.assertEqual(getattr(request, 'ip_address', None), '98.43.23.2')

    @override_settings(RT_IP_SUBSTITUTES={'34.5.2.6': '67.5.4.2'})
    def test_substitutes(self):
        from rt_ip.middleware import IPMiddleware

        request = self.factory.get('/', HTTP_REMOTE_ADDR='34.5.2.6')

        middleware = IPMiddleware()
        self.assertIsNone(middleware.process_request(request))
        self.assertEqual(getattr(request, 'ip_address', None), '67.5.4.2')