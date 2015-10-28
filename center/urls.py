from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'center.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^pessoa/$', "attend.views.pessoa"),
                       url(r'^pessoa/(?P<id_pessoa>\d+)/$', "attend.views.editaPessoa"),
                       url(r'^adiciona/$', "attend.views.adicionaPessoa"),
                       url(r'^remove/(?P<id_pessoa>\d+)/$', "attend.views.removePessoa"),
                       url(r'^admin/', include(admin.site.urls)),
                       )
