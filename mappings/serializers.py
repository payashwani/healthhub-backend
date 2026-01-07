from rest_framework import serializers
from .models import PatientDoctorMapping

from patients.models import Patient
from doctors.models import Doctor

from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(),
        source='patient',
        write_only=True
    )

    doctor = DoctorSerializer(read_only=True)

    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        source='doctor',
        write_only=True
    )

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id',
            'patient',
            'patient_id',
            'doctor',
            'doctor_id',
            'assigned_at'
        ]
        read_only_fields = ['assigned_at']

    def validate(self, attrs):
        patient = attrs['patient']
        if patient.created_by != self.context['request'].user:
            raise serializers.ValidationError(
                "You can only assign doctors to your own patients."
            )
        return attrs
