from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_patterns = [
    path('', include('quizes.api.urls')),
    path('', include('courses.api.urls')),
    path('', include('homeworks.api.urls')),
    path('', include('authentication.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
