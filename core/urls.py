from django.contrib import admin

# includ ni chaqirdik
from django.urls import path, include

# bu if debugniki
from django.conf import settings
from django.conf.urls.static import static

#bu yerda hozi app ni ichidagi urlsni registratsiya qildim
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('me.urls')),
]



#Bu kod bloklari Django’da DEBUG rejimi faolligida statik va media fayllarni xizmat ko'rsatish uchun kerak. Keling, har birini tushuntirib beram
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

