from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Review
from taggit.serializers import TagListSerializerField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = TagListSerializerField()
    progress_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['user', 'date_added', 'last_updated']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password']
    #     )
    #     return user