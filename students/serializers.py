from rest_framework import serializers
from .models import Student
from authentication.models import CustomUser

class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)  # Accept full name input

    class Meta:
        model = Student
        fields = ['full_name', 'age', 'contact', 'photo', 'documents', 'assigned_class']

    def create(self, validated_data):
        # Extract full_name and remove it from validated_data
        full_name = validated_data.pop('full_name', None)
        if not full_name:
            raise serializers.ValidationError({"full_name": "Full name is required."})

        # Split full_name into first_name and last_name
        name_parts = full_name.split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        # Create the user
        user = CustomUser.objects.create(
            username=f"student_{validated_data['contact']}",
            first_name=first_name,
            last_name=last_name,
            role='student'
        )

        # Create the student
        student = Student.objects.create(user=user, **validated_data)
        return student
