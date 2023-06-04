import debug_toolbar  # noqa
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shipments/', include('shipments.urls')),
    path('api/directions/', include('direction.urls')),
    path('api/transporters/', include('transporter.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
]
