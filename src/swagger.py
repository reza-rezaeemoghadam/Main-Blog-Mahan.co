# Importing Swagger Modules
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Importing Rest Framework modules
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)