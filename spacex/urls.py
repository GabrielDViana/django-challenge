from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('frontend.urls')),
    # path('', include('launch.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('launch.urls'))
]
