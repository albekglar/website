from rest_framework import viewsets
from .models import Languages,Framework
from .serializers import LanguagesSerializer,FrameworkSerializer


class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer 
    
    
    
class FrameworkViewSet(viewsets.ModelViewSet):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
