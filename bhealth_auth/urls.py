from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bhealth_auth.views',

    url(r'^logout/$', 'logout', name='logout'),
    url(r'^$', 'login', name='login'),

)
