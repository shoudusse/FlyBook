from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'book.views.home', name='home'),
    # url(r'^FlyBook/', include('FlyBook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
)
