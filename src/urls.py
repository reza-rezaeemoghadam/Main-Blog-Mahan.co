from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# Importing swagger schema
from src.swagger import schema_view

# Main URL patterns
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.api.v1.urls', namespace='blog')),
    path('api/v1/', include('user.api.v1.urls', namespace='user')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
)
