from django.db.models import Count
from requests import Response
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView

from .models import Review
from .serializers import ReviewSerializer, ShopSerializer
from .services import parsing


class ReviewCreateAPIView(generics.CreateAPIView):
    """
    API View to create a new Review
    permission: - Is Authenticated
    """
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]




class ReviewUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View to update a Review
    permissions: - Is Authenticated
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Review.objects.all()


# class ReviewCreateView(APIView):
#     def post(self, request):
#         shop = ShopSerializer(data=request.data)
#         shop = parsing(shop)
#         shop.save
#         review = ReviewCRUDSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)

# class DetailShopAPIView(generics.RetrieveAPIView):
#     serializer_class = ShopSerializer
    # search_fields = ['shop_name']
    # filter_backends = (filters.SearchFilter,)
    # queryset = Review.objects.all()


# class ReviewListAPIView(generics.ListAPIView):
#     """
#     API View to get shop list order by rating or review count
#     permission: - Is Authenticated
#     """
#     serializer_class = ShopListAPIViewSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
#
#     queryset = Review.objects.all()

