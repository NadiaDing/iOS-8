from django.conf.urls import patterns, include, url
from django.contrib import admin
from survey import urls as appurls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleSurvey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(appurls)),
)
