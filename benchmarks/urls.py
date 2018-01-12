from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('attributes/', include('attributes.urls')),
    path('admin/', admin.site.urls),
]