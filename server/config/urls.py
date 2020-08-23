from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.authtoken import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.api.routers import router

schema_view = get_schema_view(
   openapi.Info(
      title="API sibdev-practice",
      default_version='v1',
      description="API для поиска ближайших заведений общественного питания",
      contact=openapi.Contact(email="masterkristall@gmail.com"),
   ),
   public=True,
)

urlpatterns = [
    path('api/auth/token/', views.obtain_auth_token),
    url('^api/$', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    import debug_toolbar

    urlpatterns += [
          path('__debug__/', include(debug_toolbar.urls)),
    ]
