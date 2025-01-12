from rest_framework import serializers
from .models import Student
from authentication.models import CustomUser

class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=False)  # Accept full name input

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'age', 'contact', 'photo', 'documents', 'assigned_class']

    def create(self, validated_data):
        full_name = validated_data.pop('full_name', None)
        if not full_name:
            raise serializers.ValidationError({"full_name": "Full name is required."})

        name_parts = full_name.split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        user = CustomUser.objects.create(
            username=f"student_{validated_data['contact']}",
            first_name=first_name,
            last_name=last_name,
            role='student'
        )
        default_password = "defaultpassword123"  
        user.set_password(default_password)
        user.save()

        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        full_name = validated_data.pop('full_name', None)
        
        if full_name:
            name_parts = full_name.split(' ', 1)
            instance.user.first_name = name_parts[0]
            instance.user.last_name = name_parts[1] if len(name_parts) > 1 else ""
            instance.user.save()

        return super().update(instance, validated_data)
