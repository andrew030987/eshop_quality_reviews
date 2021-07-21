from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Review(models.Model):
    shop_link = models.CharField(max_length=50, verbose_name='Shop link', null=True, blank=True)
    user_mail = models.EmailField(max_length=50, verbose_name='User email', null=True, blank=True)
    shop = models.CharField(max_length=50, verbose_name='Shop name', blank=True, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.review_title
