from django.urls import path
from .views import ReviewCreateAPIView, ReviewUpdateDeleteAPIView, ReviewCountListAPIView, \
    ReviewListRatingAPIView, DetailShopAPIView, DetailUserAPIView

urlpatterns = [
    path('review-create/', ReviewCreateAPIView.as_view()),
    path('review-ud/<int:pk>/', ReviewUpdateDeleteAPIView.as_view()),
    path('shop-list/', ReviewCountListAPIView.as_view()),
    path('shop-rating/', ReviewListRatingAPIView.as_view()),
    path('users/search', DetailUserAPIView.as_view()),
    path('shops/search', DetailShopAPIView.as_view()),
]
