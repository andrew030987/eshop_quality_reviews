from rest_framework import serializers

from .models import Review, Shop
from .services import parsing


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['shop', 'user', 'review_title', 'review_text', 'review_stars']


class ShopSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True)
    shop = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['id', 'shop_link', 'shop', 'review']

    def get_shop(self, instance):
        return parsing(instance.shop_link)



# class ShopListAPIViewSerializer(serializers.ModelSerializer):
#     review_count = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Review
#         fields = ('review_title', 'review_count')
#
#     def get_review_count(self, obj):
#         review_count = Review.objects.filter(user__in=[obj]).count()
#         return review_count


