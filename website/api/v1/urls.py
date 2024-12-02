# Importing rest framework modules
from rest_framework.urls import path

# Importing custom views
from website.api.v1.veiws import SectionRetrieveAPIView, ContactUsCreateAPIView

# Implementing website urls
app_name = "website"

urlpatterns = [
    path('website/<int:pk>/', SectionRetrieveAPIView.as_view(), name="section_retrieve"),
    path('website/contact-us/', ContactUsCreateAPIView.as_view(), name="contact_us_create"),
]