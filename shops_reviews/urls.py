from django.urls import path
from .views import ReviewCreateAPIView, ReviewUpdateDeleteAPIView, ReviewCountListAPIView, \
    ReviewListRatingAPIView, DetailShopAPIView, DetailUserAPIView

urlpatterns = [
    path('review-create/', ReviewCreateAPIView.as_view(), name='create'),
    path('review-ud/<int:pk>/', ReviewUpdateDeleteAPIView.as_view(), name='update_destroy'),
    path('shop-list/', ReviewCountListAPIView.as_view(), name='shop_list'),
    path('shop-rating/', ReviewListRatingAPIView.as_view(), name='shop_rating'),
    path('users/search', DetailUserAPIView.as_view(), name='users_search'),
    path('shops/search', DetailShopAPIView.as_view(), name='shop_search'),
]
