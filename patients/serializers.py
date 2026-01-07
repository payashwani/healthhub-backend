from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'gender', 'phone', 'address', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']