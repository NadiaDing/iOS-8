from django.conf.urls import patterns, include, url
from share import urls as appurls
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from settings import MEDIA_URL, MEDIA_ROOT
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ImageShare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include(appurls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)