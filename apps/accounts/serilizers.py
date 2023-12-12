from rest_framework import serializers
from .models import User

class UserSetializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'email']
        read_only_fields = ["id"]





