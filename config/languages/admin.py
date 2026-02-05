
from django.contrib import admin
from .models import Languages, Framework


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    # Отображение в списке
    list_display = ('name', 'date')
    
    # Поля в форме редактирования
    fields = ('name', 'description', 'date')



@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    # Отображение в списке
    list_display = ('title', 'languages', 'date')

    # Поля в форме редактирования
    fields = ('title', 'languages', 'description', 'date')

