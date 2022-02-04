from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'password', 
            'role',
            'level',
            'updated_at',
            'created_at'
        ]
        
class LoginSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['email', 'password']