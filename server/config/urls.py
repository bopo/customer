# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import stock.service.urls
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from stock.wechat import views
import django
import stock.frontend.views

urlpatterns = (
    url(r'^api/wechat/$', views.home),
    url(r'^api/', include(stock.service.urls)),
    url(r'^account/signup/$', stock.frontend.views.signup),
    url(r'^account/verify/$', stock.frontend.views.verify),

    url(r'^account/success/(?P<openid>.*)/$', stock.frontend.views.success),
    url(r'^account/errors/', stock.frontend.views.errors),
    
    url(r'^account/union/$', stock.frontend.views.union),
    
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    
    if ('debug_toolbar' in settings.INSTALLED_APPS):
        import debug_toolbar
        urlpatterns += (url(r'^__debug__/', include(debug_toolbar.urls)),)
# else:
#     urlpatterns += [
#         url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
#         url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permissin Denied")}),
#         url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
#         url(r'^500/$', default_views.server_error),
#     ]
