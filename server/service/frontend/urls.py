from django.conf.urls import url

import views

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
    url(r'^manage/$', views.home, name='home'),
    url(r'^manage/history/', views.history, name='history'),
    url(r'^manage/report/', views.report, name='report'),
    url(r'^manage/me/', views.me, name='me'),

    url(r'^qr_check/(?P<uuid>.*?)/', views.qr_check, name='qr_check'),
    url(r'^qr_login/', views.qr_login, name='qr_login'),
    url(r'^qr_done/', views.qr_done, name='qr_done'),

    url(r'^detail/(?P<id>\d+)', views.detail, name='detail'),
    url(r'^support/$', views.support, name='support'),
    url(r'^goods/', views.goods, name='goods'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^buy/success/(?P<token>.*?)/$', views.buy_success, name='buy_success'),
    url(r'^buy/confirm/(?P<token>.*?)/$', views.buy_confirm, name='buy_confirm'),
    url(r'^buy/errors/$', views.buy_errors, name='buy_errors'),
    url(r'^buy/close/(?P<token>.*?)/$', views.buy_close, name='buy_close'),
    url(r'^buy/save/$', views.buy_save, name='buy_save'),

    # url(r'^channel/(?P<id>\d+)', 'frontend.views.channel', name='category'),
    # url(r'^detail/(?P<id>\d+)', 'frontend.views.detail', name='detail'),
    # url(r'^detail/(?P<id>\d+\.html)', 'frontend.views.detail', name='detail'),

    # url(r'^share/extract', 'frontend.views.share_extract', name='share_extract'),
    # url(r'^share/invite', 'frontend.views.share_invite', name='share_invite'),
    # url(r'^share/prize', 'frontend.views.share_prize', name='share_prize'),
    # url(r'^q', 'frontend.views.q', name='q'),
]
