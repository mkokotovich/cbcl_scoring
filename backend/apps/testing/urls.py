from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/', include('apps.testing.v1_urls')),
]
