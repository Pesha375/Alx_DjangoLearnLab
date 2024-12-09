from django.contrib import admin
from django.urls import path, include  # Include `include`

urlpatterns = [
    path('admin/', admin.site.urls),            # Admin panel
    path('api/', include('api.urls')),          # Include API routes from `api/urls.py`
]


