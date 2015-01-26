from django.conf.urls import patterns, include, url

#from store import urls as app_urls
from django.contrib import admin
from store import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleStore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
                       #url(r'^$', include(app_urls)),
    url(r'^$', views.catalog, name='catalog'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^cart/remove/$',views.removefromcart,name="remove"),
    url(r'^cart/checkout/$', views.checkout, name='checkout'),
    url(r'^cart/checkout/complete/$', views.completeOrder, name='complete_order'),
    url(r'^admin_login/$',views.adminLogin,name='admin_login'),
    url(r'^admin_panels/$',views.adminDashboard,name='admin'),
    
    
)
