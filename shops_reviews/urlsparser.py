from urllib.parse import urlparse


def parsing(url):
    url = urlparse(url).netloc
    a = url.split('.')
    if len(a) >= 3:
        a = a[:-(len(a)-1)]
    else:
        a = a[:-1]
    x = ('.'.join(a))
    return x
