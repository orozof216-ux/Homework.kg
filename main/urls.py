from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('books/', include('books.urls')),
    path('blog/', include('blog.urls')),
    path('auto/', include('auto.urls')),
    path('tours/', include('horse_tour.urls')),
    path('booking/', include('booking.urls')),
    path('donates/', include('donates.urls')),
    path('users/', include('users.urls')),
    path('resume/', include('resume.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 