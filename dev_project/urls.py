from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.urls import path 
from .views.resource_count import create_resource_count
from .views.day_count import create_day_count

urlpatterns = [
    url(r'^', include('arches.urls')),
    path("resource_count/", create_resource_count, name="resource_count"),
    path("day_count/", create_day_count, name="day_count")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SHOW_LANGUAGE_SWITCH is True:
    urlpatterns = i18n_patterns(*urlpatterns)

