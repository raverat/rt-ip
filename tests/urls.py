from django.conf.urls import url


urlpatterns = [
    url(r'^/$', 'tests.views.index', name='index'),
]