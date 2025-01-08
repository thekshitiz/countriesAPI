from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('countries.urls')),  # Use `path` for including routes
    path('api/', include('api.urls')),    # No need for `url`
]
