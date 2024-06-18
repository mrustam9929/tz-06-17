from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import include, path, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.unregister(Group)
admin.site.site_header = 'Админ панель'
admin.site.site_title = 'Админ панель'
admin.site.index_title = 'Админ панель'
