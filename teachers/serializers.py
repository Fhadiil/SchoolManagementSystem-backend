from rest_framework import serializers
from .models import Teacher, Subject
from authentication.models import CustomUser
from classes.models import Class
import uuid
import secrets  # For generating secure random passwords


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True)
    assigned_classes = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), many=True, required=False)

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'qualifications', 'contact', 'photo', 'subjects', 'assigned_classes']

    def generate_unique_username(self, base_username):
        """Generate a unique username by appending a suffix if needed."""
        username = base_username
        while CustomUser.objects.filter(username=username).exists():
            unique_suffix = uuid.uuid4().hex[:6]  # Generate a random 6-character suffix
            username = f"{base_username}_{unique_suffix}"
        return username

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        subjects = validated_data.pop('subjects', [])
        assigned_classes = validated_data.pop('assigned_classes', [])

        # Split full name into first and last names
        try:
            first_name, last_name = full_name.split(' ', 1)
        except ValueError:
            raise serializers.ValidationError("Full name must include both first and last names.")

        # Generate a unique username based on contact
        contact = validated_data.get('contact', '')
        base_username = f"teacher_{contact}_sms"
        username = self.generate_unique_username(base_username)

        # Generate a random secure password
        random_password = secrets.token_urlsafe(12)  # Generates a 12-character secure password

        # Create the CustomUser instance
        user = CustomUser.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            role='teacher'
        )
        user.set_password(random_password)
        user.save()

        # Create the Teacher profile
        teacher = Teacher.objects.create(user=user, **validated_data)
        teacher.subjects.set(subjects)
        teacher.assigned_classes.set(assigned_classes)
        return teacher

    def update(self, instance, validated_data):
        full_name = validated_data.pop('full_name', None)
        subjects = validated_data.pop('subjects', None)
        assigned_classes = validated_data.pop('assigned_classes', None)

        if full_name:
            try:
                first_name, last_name = full_name.split(' ', 1)
                instance.user.first_name = first_name
                instance.user.last_name = last_name
                instance.user.save()
            except ValueError:
                raise serializers.ValidationError("Full name must include both first and last names.")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if subjects is not None:
            instance.subjects.set(subjects)
        if assigned_classes is not None:
            instance.assigned_classes.set(assigned_classes)

        instance.save()
        return instance
