from django.urls import path
from .views import (
    MappingListCreateView,
    MappingPatientDoctorsView,
    MappingDetailView
)

urlpatterns = [
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', MappingPatientDoctorsView.as_view(), name='mapping-patient-doctors'),
    path('mappings/<int:pk>/', MappingDetailView.as_view(), name='mapping-detail'),  # for DELETE
]