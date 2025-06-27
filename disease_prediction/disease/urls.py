from django.urls import path
from .views import CheckDiseaseAPIView

urlpatterns = [
    path('checkdisease/', CheckDiseaseAPIView.as_view(), name='checkdisease'),
]