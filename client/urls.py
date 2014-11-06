from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/$', 'client.views.profile', name='profile'),

)
