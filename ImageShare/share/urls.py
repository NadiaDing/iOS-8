from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ImageShare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.upload, name="main"),
    url(r'^upload/$',views.hnd_load,name="upload"),
    
)


