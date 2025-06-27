from django.urls import path
from .views import NLPBased

urlpatterns = [
    # path('checkdisease/', CheckDiseaseAPIView.as_view(), name='checkdisease'),
    path('nlp/', NLPBased.as_view(), name='nlp_based'),

]