# Importing rest framework modules
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView

# Importing custom Serializers
from website.api.v1.serializers import FullPortionSectionSerializers ,FullPortionContactUsSerializer

# Importing custom models
from website.models import Section, ContactUs

# Implementing views
class SectionRetrieveAPIView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = FullPortionSectionSerializers
    permission_classes = [AllowAny]


class ContactUsCreateAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = FullPortionContactUsSerializer
    permission_classes = [AllowAny]