from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/', include('books.urls')),
    path('', include('blog.urls')),
    path('', include('auto.urls')),

    path('tours/', include('horse_tour.urls')),
    path('booking/', include('booking.urls')),
    path('', include('donates.urls')),
    path('', include('users.urls')),

    path('resume/', include('resume.urls')),

    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)