"""
Модуль serializer.

Предназначен для преобразования данных моделей Python в JSON и обратно.
В моделях представлены поля которые можно сериализовать.
"""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.
    Преобразует данные о продукте в JSON формат и обратно.
    """

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'author', 'created_at']
