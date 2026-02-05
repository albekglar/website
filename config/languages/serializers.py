from rest_framework import serializers
from .models import Languages,Framework

"""Создаем сериализацию для  модели languages(языки)"""
class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ['id','name','description','description']
        
        
        
"""Создаем  сериализацию для модели Framework (библиотеки)""" 
class FrameworkSerializer(serializers.ModelSerializer):
    
    languages = LanguagesSerializer(read_only=True)
    
    class Meta:
        model = Framework
        fields = ['id','title','description','languages','date']
    
