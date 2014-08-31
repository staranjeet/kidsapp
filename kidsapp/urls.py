from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kidsapp import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kidsapp.views.parallax', name='parallax'),
    url(r'level1', 'kidsapp.views.level1', name='level1'),
    url(r'levelaa', 'kidsapp.views.level11', name='level11'),
    url(r'levelab', 'kidsapp.views.level12', name='level12'),
    url(r'levelac', 'kidsapp.views.level13', name='level13'),
    url(r'levelad', 'kidsapp.views.level14', name='level14'),    
    url(r'levelae', 'kidsapp.views.level15', name='level14'),

    url(r'level2', 'kidsapp.views.level2', name='level2'),
    url(r'levels', 'kidsapp.views.levels', name='levels'), 
	url(r'levelba', 'kidsapp.views.level21', name='level21'),
    url(r'levelbb', 'kidsapp.views.level22', name='level22'),
    url(r'levelbc', 'kidsapp.views.level23', name='level23'),
    url(r'levelbd', 'kidsapp.views.level24', name='level24'),
    url(r'levelbe', 'kidsapp.views.level25', name='level14'),

    url(r'level3', 'kidsapp.views.level3', name='level3'),
    url(r'levelca', 'kidsapp.views.level31', name='level31'),
    url(r'levelcb', 'kidsapp.views.level32', name='level32'),
    url(r'levelcc', 'kidsapp.views.level33', name='level33'),
    url(r'levelcd', 'kidsapp.views.level34', name='level34'),
    
    url(r'level4', 'kidsapp.views.level4', name='level4'),
    url(r'levelda', 'kidsapp.views.level41', name='level41'),
    url(r'leveldb', 'kidsapp.views.level42', name='level42'),
    url(r'leveldc', 'kidsapp.views.level43', name='level43'),
    url(r'leveldd', 'kidsapp.views.level44', name='level44'),
    url(r'levelde', 'kidsapp.views.level45', name='level45'),
    url(r'par', 'kidsapp.views.parallax', name='parallax'),




    # url(r'^kidsapp/', include('kidsapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
