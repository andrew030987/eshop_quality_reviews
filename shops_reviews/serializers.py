from rest_framework import serializers
from .models import Review
from .service import parsing


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    shop = serializers.SerializerMethodField()

    def get_shop(self, obj):
        return obj.shop

    class Meta:
        model = Review
        fields = ['shop_link', 'shop', 'user_mail', 'review_title', 'review_text', 'review_stars', 'user']

    def create(self, validated_data):
        return Review.objects.create(**validated_data, shop=parsing(validated_data.get('shop_link')))


class ReviewUpdateDeleteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ['shop_link', 'shop', 'user_mail', 'review_title', 'review_text', 'review_stars', 'user']


class ShopListReviewSerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ['shop', 'review_count']


class ShopListRatingSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        model = Review
        fields = ['shop', 'rating']


class DetailReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ['shop_link', 'shop', 'user_mail', 'review_title', 'review_text', 'review_stars', 'user', 'review_dt']