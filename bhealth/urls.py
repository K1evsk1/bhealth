from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('client.urls', namespace='client')),
    url(r'^product/', include('product.urls', namespace='product'))
)

#authentification
urlpatterns += patterns('',
    url(r'^', include('bhealth_auth.urls', namespace='bhealth_auth'))
)

#social_authentification
urlpatterns += patterns('',
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)