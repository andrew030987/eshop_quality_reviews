from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['shop_link', 'user', 'review_title', 'review_text', 'review_stars']


class ShopListAPIViewSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('review_title', 'review_count')

    def get_review_count(self, obj):
        review_count = Review.objects.filter(user__in=[obj]).count()
        return review_count

