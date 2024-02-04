from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='blog-home'),
# ]

