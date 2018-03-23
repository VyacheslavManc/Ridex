from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ('id', 'name')


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        field = ('id', 'Name', 'Prise', )