# Importing rest framework modules
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

# Importing custom Serializers
from website.api.v1.serializers import FullPortionSectionSerializers  

# Importing custom models
from website.models import Section

# Implementing views
class SectionRetrieveAPIView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = FullPortionSectionSerializers
    permission_classes = [AllowAny]