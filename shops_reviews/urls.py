from django.urls import path
from rest_framework.generics import RetrieveAPIView

from .views import ReviewCreateAPIView, ReviewUpdateDeleteAPIView, ReviewListAPIViewSerializer, \
    ReviewListRatingAPIViewSerializer, DetailShopAPIView

urlpatterns = [
    path('review-create/', ReviewCreateAPIView.as_view()),
    path('review-ud/<int:pk>/', ReviewUpdateDeleteAPIView.as_view()),
    path('shops/<int:pk>', DetailShopAPIView.as_view()),
    path('shop-list/', ReviewListAPIViewSerializer.as_view()),
    path('shop-rating/', ReviewListRatingAPIViewSerializer.as_view())
]