from django.db.models import Count, Avg
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import Review
from .serializers import ReviewCreateSerializer, ShopListRatingSerializer, \
    ReviewUpdateDeleteSerializer, ShopListReviewSerializer, DetailReviewSerializer
from .service import ShopFilter, UserFilter
from .permissions import IsOwnerOrReadOnly


class ReviewCreateAPIView(generics.CreateAPIView):
    """
    API View to create a new Review
    permission: - Is Authenticated
    """
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticated,)


class ReviewUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View to update or delete a Review
    permissions: - Is Owner or Admin
    """
    serializer_class = ReviewUpdateDeleteSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)
    queryset = Review.objects.all()


class ReviewCountListAPIView(generics.ListAPIView):
    """
    API View to get shop list ordered by review count
    permission: - Is Authenticated
    """
    serializer_class = ShopListReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Review.objects.values('shop').annotate(review_count=Count('shop')).order_by('-review_count')

        return queryset


class ReviewListRatingAPIView(generics.ListAPIView):
    """
    API View to get shop list ordered by rating
    permission: - Is Authenticated
    """
    serializer_class = ShopListRatingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    """
    Calculating and annotating average shop rating, ordering results by rating
    """
    def get_queryset(self):
        queryset = Review.objects.values('shop').annotate(rating=Avg('review_stars')).order_by('-rating')

        return queryset


class DetailUserAPIView(generics.ListAPIView):
    """
    API View to get review list filter by user, ordered by datetime
    permission: - Is Authenticated
    """
    queryset = Review.objects.all().order_by('-review_dt')
    serializer_class = DetailReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = UserFilter


class DetailShopAPIView(generics.ListAPIView):
    """
    API View to get review list filter by shop name
    permission: - Is Authenticated
    """
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = ShopFilter
