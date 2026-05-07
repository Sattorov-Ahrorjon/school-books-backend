from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, CategoryViewSet, BookViewSet

router = DefaultRouter()

router.register(r'class', ClassViewSet, basename='class')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'book', BookViewSet, basename='book')

urlpatterns = router.urls
