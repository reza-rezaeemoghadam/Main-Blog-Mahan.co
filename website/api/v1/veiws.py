# Importing rest framework modules
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

# Importing custom Serializers
from website.api.v1.serializers import FullPortionSectionSerializers  

# Importing custom models
from website.models import Section

# Implementing views
class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = FullPortionSectionSerializers
    permission_classes = [AllowAny]
    model = Section