from .models import User,Book
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=['username','password']


class BookSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model=Book
        fields=['id','title','description','author','price']

class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password","password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializer.ValidationError("Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


