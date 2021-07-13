from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Shop(models.Model):
    shop_link = models.CharField(max_length=50, verbose_name='Shop link', null=True, blank=True)

    def __str__(self):
        return self.shop_link


class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    user = models.EmailField(max_length=50, verbose_name='User', null=True, blank=True)
    review_title = models.CharField(max_length=50, verbose_name='Review title')
    review_text = models.CharField(max_length=255, verbose_name='Review text')
    STARS = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    review_stars = models.IntegerField(choices=STARS, verbose_name='Stars')
    review_dt = models.DateTimeField(auto_now=True, verbose_name='Review created at')

    def __str__(self):
        return self.review_title
