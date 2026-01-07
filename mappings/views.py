from rest_framework import generics, permissions
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

class MappingPatientDoctorsView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)

class MappingDetailView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    permission_classes = [permissions.IsAuthenticated]