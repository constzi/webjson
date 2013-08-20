from django.conf.urls import patterns, include, url
from data.models import Info, Detail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
admin.site.register(Info)
admin.site.register(Detail)
'''admin login: charlie / brown '''

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tester/$', 'data.views.tester'),
    url(r'^data/$', 'data.views.index'),
    url(r'^trends/$', 'data.views.trends'),
)
