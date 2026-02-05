from django.db import models


"""Создаем модель languages(языки)"""
class Languages(models.Model):
    
    # название
    name = models.CharField(max_length=20)
    
    # описание
    description = models.TextField(blank=True)
    
    # дата 
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
"""Создаем модель Framework (библиотеки)"""  
class Framework(models.Model):
    
    # название библиотеки
    title = models.CharField(max_length=255)
    
    # языки
    languages = models.ForeignKey(Languages,on_delete=models.CASCADE)
    
     # описание
    description = models.TextField(blank=True)
    
    # дата 
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    