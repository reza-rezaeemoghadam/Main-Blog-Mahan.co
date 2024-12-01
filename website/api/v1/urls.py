# Importing rest framework modules
from rest_framework.urls import path

# Importing custom views
from website.api.v1.veiws import SectionRetrieveAPIView

# Implementing website urls
app_name = "website"

urlpatterns = [
    path('website/<int:section_id>/', SectionRetrieveAPIView.as_view(), name="section_retrieve"),
]