from urllib.parse import urlparse
import django_filters
from .models import Review


def parsing(url):
    """
    URL parser to get a shop name from the shop's link
    """

    url = urlparse(url).netloc
    a = url.split('.')
    if len(a) >= 3:
        a = a[:-(len(a) - 1)]
    else:
        a = a[:-1]
    x = ('.'.join(a))
    return x


class ShopFilter(django_filters.FilterSet):
    """
    Shop filter to search by shop name
    """

    shop = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Review
        fields = ('shop',)


class UserFilter(django_filters.FilterSet):
    """
    User filter to search by either user email field or user name
    """

    user_mail = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Review
        fields = ('user_mail', 'user')
