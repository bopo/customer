from django.conf.urls import url
from .views import *
# sitemaps = {'static': PhotoViewSitemap,}

# urlpatterns = patterns('',
#     url(r'^$', 'frontend.views.home', name='home'),
#     url(r'^category/(?P<slug>\w+)', 'frontend.views.category', name='category'),
#     url(r'^detail/(?P<id>\d+)', 'frontend.views.detail', name='detail'),
#     url(r'^detail/(?P<id>\d+\.html)', 'frontend.views.detail', name='detail'),
#
#         # url(r'^feed/rss$', RSS()),
#         # url(r'^feed/rss\.xml$', RSS()),
#         # url(r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap',
#         #     {'sitemaps': sitemaps}),
#     )

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^history/', history, name='history'),
    url(r'^report/', report, name='report'),
    url(r'^me/', me, name='me'),
    url(r'^qr_login/', qr_login, name='qr_login'),
    url(r'^qr_done/', qr_done, name='qr_done'),
    url(r'^qr_check/(?P<uuid>.*?)/', qr_check, name='qr_check'),

    # url(r'^channel/(?P<id>\d+)', 'frontend.views.channel', name='category'),
    # url(r'^detail/(?P<id>\d+)', 'frontend.views.detail', name='detail'),
    # url(r'^detail/(?P<id>\d+\.html)', 'frontend.views.detail', name='detail'),

    # url(r'^share/extract', 'frontend.views.share_extract', name='share_extract'),
    # url(r'^share/invite', 'frontend.views.share_invite', name='share_invite'),
    # url(r'^share/prize', 'frontend.views.share_prize', name='share_prize'),
    # url(r'^q', 'frontend.views.q', name='q'),
]
