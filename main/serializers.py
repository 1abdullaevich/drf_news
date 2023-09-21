from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'age']
