"""
URL configuration for LMS_BACK project.
"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Create a simple root view
from django.http import JsonResponse
def home(request):
    return JsonResponse({
        "status": "OK",
        "message": "Backend Running Successfully"
    })

urlpatterns = [
    # Root URL
    path('', home, name='home'),          # <-- Fixes Not Found /

    # API endpoints
    path('api/auth/', include('authentication.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/quizzes/', include('quizzes.urls')),
    path('api/progress/', include('progress.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/ai-assistant/', include('ai_assistant.urls')),
]

# Serve media/static in Debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
