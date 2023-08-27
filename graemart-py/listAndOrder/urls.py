"""
URL configuration for listAndOrder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('graeMart/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # admin endpoint.
    path('admin/', admin.site.urls),

    # auth endpoints.
    path('graeMart_api/v1/auth/', include('users.urls')),

    # profile endpoints.
    path('graeMart_api/v1/profile/', include('vendor_profile.urls')),

    # support endpoints.
    path('graeMart_api/v1/suport/', include('support.urls')),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
#                static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)