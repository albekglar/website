from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LanguagesViewSet,FrameworkViewSet


router = DefaultRouter()
router.register('Languages',LanguagesViewSet)
router.register('Framework',FrameworkViewSet)

urlpatterns = [
    path('',include(router.urls))

]