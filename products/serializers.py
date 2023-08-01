from rest_framework import serializers
from . import models


class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("name", "slug", "description", "children")


class CategorySerializer(serializers.ModelSerializer):
    children = NestedCategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ["name", "slug", "description", "parent", "children"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ["user", "content"]


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ["name", "description", "price", "images", "comments"]


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Brand
        field = "__all__"
