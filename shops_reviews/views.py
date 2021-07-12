from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Review
from .serializers import ReviewSerializer, ShopListAPIViewSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    """
    API View to create a new Review
    permission: - Is Authenticated
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ReviewUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View to update a Review
    permissions: - Is Authenticated
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Review.objects.all()


class DetailShopAPIView(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    search_fields = ['shop_name']
    filter_backends = (filters.SearchFilter,)
    pass


class ReviewListAPIView(generics.ListAPIView):
    """
    API View to get shop list order by rating or review count
    permission: - Is Authenticated
    """
    serializer_class = ShopListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    pass

