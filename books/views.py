from rest_framework import viewsets, mixins
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from .models import Class, Category, Book
from .serializers import ClassSerializer, CategorySerializer, BookSerializer, BookFilter


class CustomViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    pass


@extend_schema(tags=['class'])
class ClassViewSet(CustomViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


@extend_schema(tags=['category'])
class CategoryViewSet(CustomViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['book'])
class BookViewSet(CustomViewSet):
    queryset = Book.objects.select_related('class_name', 'category')
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
