from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.Users.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('QLA/', include('apps.QLA.urls')),
    path('Contact/', include('apps.Contactus.urls')),
    path('Subscription/', include('apps.Subscription.urls')),
    path('Bundle/', include('apps.bundle.urls')),
    path('payments/', include('apps.payments.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
