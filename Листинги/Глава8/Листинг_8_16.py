from django.contrib import admin
from django.urls import include, path
# добавлено для работы с медиа файлами
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('firstapp.urls')),
    path('admin/', admin.site.urls),
]

# добавлено для работы с медиа файлами локально
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
