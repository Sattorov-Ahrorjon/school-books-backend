from rest_framework import serializers
from .models import Class, Category, Book


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    class_name_str = serializers.CharField(source='class_name.name', read_only=True)
    category_str = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Book
        fields = (
            'id', 'name', 'image', 'about', 'publication', 'file', 'class_name',
            'class_name_str', 'category', 'category_str'
        )
