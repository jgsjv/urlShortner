from django.conf.urls import patterns, include, url

urlpatterns = patterns('shortenerSite.views',
    url(r'^$', 'index', name='home'),
 
    url(r'^(?P<short_id>\w{6})$', 'redirectOriginal', name='redirectOriginal'),
 
    url(r'^makeshort/$', 'shortenUrl', name='shortenUrl'),
)