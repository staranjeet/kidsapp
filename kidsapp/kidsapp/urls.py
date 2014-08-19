from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kids.views.home', name='home'),
    url(r'level1', 'kids.views.level1', name='level1'),
    url(r'level2', 'kids.views.level2', name='level2'),
    url(r'level3', 'kids.views.level3', name='level3'),
    url(r'level4', 'kids.views.level4', name='level4'),
    url(r'parallax', 'kids.views.parallax', name='level4'),


    # url(r'^kidsapp/', include('kidsapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
