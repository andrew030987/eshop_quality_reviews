from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class ReviewCreateTest(APITestCase):
    def setUp(self):
        self.user_data = {
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user_mail": "user42@mail.ru",
            "review_title": "Good",
            "review_text": "Very good shop",
            "review_stars": 5
        }
        self.user = User.objects.create_user(
            'user0112', 'user01@example.com', 'user01P4ssw0rD')

    def tearDown(self):
        return super().tearDown()

    def test_review_create_positive(self):
        self.client.force_authenticate(self.user)
        res = self.client.post(reverse('create'), self.user_data, format='json')
        self.assertEqual(res.status_code, 201)

    def test_review_create_negative_blank_field(self):
        user_data = {
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user_mail": "",
            "review_title": "Good",
            "review_text": "Very good shop",
            "review_stars": 5
        }

        self.client.force_authenticate(self.user)
        res = self.client.post(reverse('create'), user_data, format='json')

        self.assertEqual(res.status_code, 400)

    def test_review_create_negative_not_auth(self):
        res = self.client.post(reverse('create'), self.user_data, format='json')
        self.assertEqual(res.status_code, 403)


class ReviewShopListTest(APITestCase):

    def test_shop_list(self):
        user_data = {
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user_mail": "user42@mail.ru",
            "review_title": "Good",
            "review_text": "Very good shop",
            "review_stars": 5
        }
        user = User.objects.create_user(
            'user01', 'user01@example.com', 'user01P4ssw0rD')
        self.client.force_authenticate(user)
        self.client.post(reverse('create'), user_data, format='json')
        res = self.client.get(reverse('shop_list'))
        self.assertEqual(res.status_code, 200)


class ReviewShopRatingTest(APITestCase):

    def test_shop_list(self):
        user_data = {
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user_mail": "user42@mail.ru",
            "review_title": "Good",
            "review_text": "Very good shop",
            "review_stars": 5
        }
        user = User.objects.create_user(
            'user01', 'user01@example.com', 'user01P4ssw0rD')
        self.client.force_authenticate(user)
        self.client.post(reverse('create'), user_data, format='json')
        res = self.client.get(reverse('shop_rating'))
        self.assertEqual(res.status_code, 200)


class ReviewShopFilterTest(APITestCase):

    def test_shop_list(self):
        user_data = {
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user_mail": "user42@mail.ru",
            "review_title": "Good",
            "review_text": "Very good shop",
            "review_stars": 5
        }
        user = User.objects.create_user(
            'user01', 'user01@example.com', 'user01P4ssw0rD')
        self.client.force_authenticate(user)
        self.client.post(reverse('create'), user_data, format='json')
        res = self.client.get('http://127.0.0.1:8000/api/v1/reviews/shops/search?shop=rozetka')
        self.assertEqual(res.status_code, 200)


class ReviewUserFilterTest(APITestCase):

    def test_shop_list(self):
        user_data = {
            "shop_link": "https://rozetka.com.ua/tovary-dlia-koshek/",
            "user_mail": "user42@mail.ru",
            "review_title": "Good",
            "review_text": "Very good shop",
            "review_stars": 5
        }
        user = User.objects.create_user(
            'user01', 'user01@example.com', 'user01P4ssw0rD')
        self.client.force_authenticate(user)
        self.client.post(reverse('create'), user_data, format='json')
        res = self.client.get('http://127.0.0.1:8000/api/v1/reviews/users/search?user_mail=shooter_a%40mail.ru&user=')
        self.assertEqual(res.status_code, 200)
