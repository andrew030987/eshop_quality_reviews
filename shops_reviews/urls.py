from django.urls import path
from rest_framework.generics import RetrieveAPIView

from .views import ReviewCreateAPIView, ReviewUpdateDeleteAPIView

urlpatterns = [
    path('review-create/', ReviewCreateAPIView.as_view()),
    path('review-ud/<int:pk>/', ReviewUpdateDeleteAPIView.as_view()),
    # path('shops/<int:pk>', DetailShopAPIView.as_view()),
    # path('review_list/', ReviewListAPIView.as_view()),
]