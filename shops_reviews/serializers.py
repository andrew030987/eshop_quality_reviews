from rest_framework import serializers
from .models import Review
from .service import parsing


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Binding a current user to a review that is being created"""
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    """Getting a shop name"""
    shop = serializers.SerializerMethodField()
    def get_shop(self, obj):
        return obj.shop

    class Meta:
        model = Review
        fields = ['shop_link', 'shop', 'user_mail', 'review_title', 'review_text', 'review_stars', 'user']

    """Creating a shop name by parsing it from URL and adding to a table"""
    def create(self, validated_data):
        return Review.objects.create(**validated_data, shop=parsing(validated_data.get('shop_link')))



class ReviewUpdateDeleteSerializer(serializers.ModelSerializer):
    """Showing username instead of user id"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ['shop_link', 'shop', 'user_mail', 'review_title', 'review_text', 'review_stars', 'user']



class ShopListReviewSerializer(serializers.ModelSerializer):
    """Adding review count filed to serializer"""
    review_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ['shop', 'review_count']



class ShopListRatingSerializer(serializers.ModelSerializer):
    """Adding rating field with appropriate format to serializer"""
    rating = serializers.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        model = Review
        fields = ['shop', 'rating']



class DetailReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ['shop_link', 'shop', 'user_mail', 'review_title', 'review_text', 'review_stars', 'user', 'review_dt']