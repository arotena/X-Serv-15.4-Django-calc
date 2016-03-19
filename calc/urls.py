from django.conf.urls import patterns, include, url
from operaciones import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'calc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(\d+)\+(\d+)$', views.suma),
    url(r'^(\d+)-(\d+)$', views.resta),
    url(r'^(\d+)\*(\d+)$', views.multiplicacion),
    url(r'^(\d+)/(\d+)$', views.division),
    url(r'^$', views.explicacion),
    url(r'', views.notFound),
)
