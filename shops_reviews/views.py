from django.db.models import Count, Avg
from requests import Response
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView

from .models import Review
from .serializers import ReviewSerializer, ShopListSerializer, ShopListRatingSerializer
from .services import parsing


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


class ReviewListAPIViewSerializer(generics.ListAPIView):
    serializer_class = ShopListSerializer

    def get_queryset(self):
        queryset = Review.objects.values('shop').annotate(review_count=Count('shop')).order_by('-review_count')

        return queryset


class ReviewListRatingAPIViewSerializer(generics.ListAPIView):
    serializer_class = ShopListRatingSerializer

    def get_queryset(self):
        queryset = Review.objects.values('shop').annotate(rating=Avg('review_stars')).order_by('-rating')

        return queryset


class DetailShopAPIView(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    search_fields = ['shop']
    filter_backends = (filters.SearchFilter,)
    queryset = Review.objects.all()



# class DetailShopAPIView(generics.RetrieveAPIView):
#     serializer_class = ReviewSerializer
#
#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Review.objects.all()
#         shop = self.request.query_params.get('shop')
#         if shop is not None:
#             queryset = queryset.filter(shop__shop=shop)
#         return queryset


# class ReviewCreateView(APIView):
#     def post(self, request):
#         shop = ShopSerializer(data=request.data)
#         shop = parsing(shop)
#         shop.save
#         review = ReviewCRUDSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)



# class ShopListAPIView(generics.ListAPIView):
#     """
#     API View to get shop list order by rating or review count
#     permission: - Is Authenticated
#     """
#     serializer_class = ShopSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
#
#     queryset = Shop.objects.all()
