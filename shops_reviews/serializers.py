from time import timezone

from rest_framework import serializers

from .models import Review
from .services import parsing


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['shop_link', 'user_mail', 'review_title', 'review_text', 'review_stars']

    def create(self, validated_data):
        return Review.objects.create(**validated_data, shop=parsing(validated_data.get('shop_link')))


class ShopListSerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ['shop', 'review_count']


class ShopListRatingSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        model = Review
        fields = ['shop', 'rating']
