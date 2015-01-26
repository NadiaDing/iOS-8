from django.conf.urls import patterns, include, url
from django.contrib import admin
from board import urls as appurls
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MessageBoard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include(appurls)),
    url(r'^admin/', include(admin.site.urls)),
)
