from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'demo.views.index'),
    (r'^login/$', 'demo.views.login'),
    (r'^tamper/$', 'demo.views.tamper'),
)
