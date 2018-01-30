from django.urls import include, path
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    path('attributes/', include('attributes.urls')),
    url(r'^$', include('results.urls')),
    path('admin/', admin.site.urls),
]