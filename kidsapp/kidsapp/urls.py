from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'kids.views.parallax', name='parallax'),
    url(r'^$', 'kids.views.parallax', name='parallax'),
    url(r'level1', 'kids.views.level1', name='level1'),
    url(r'levelaa', 'kids.views.level11', name='level11'),
    url(r'levelab', 'kids.views.level12', name='level12'),
    url(r'levelac', 'kids.views.level13', name='level13'),
    url(r'levelad', 'kids.views.level14', name='level14'),    
    url(r'levelae', 'kids.views.level15', name='level14'),

    url(r'level2', 'kids.views.level2', name='level2'),
    url(r'levels', 'kids.views.levels', name='levels'), 
	url(r'levelba', 'kids.views.level21', name='level21'),
    url(r'levelbb', 'kids.views.level22', name='level22'),
    url(r'levelbc', 'kids.views.level23', name='level23'),
    url(r'levelbd', 'kids.views.level24', name='level24'),
    url(r'levelbe', 'kids.views.level25', name='level14'),
    url(r'level3', 'kids.views.level3', name='level3'),
    url(r'levelca', 'kids.views.level31', name='level31'),
    url(r'levelcb', 'kids.views.level32', name='level32'),
    url(r'levelcc', 'kids.views.level33', name='level33'),
    url(r'levelcd', 'kids.views.level34', name='level34'),
    url(r'level4', 'kids.views.level4', name='level4'),
    url(r'levelda', 'kids.views.level41', name='level41'),
    url(r'leveldb', 'kids.views.level42', name='level42'),
    url(r'leveldc', 'kids.views.level43', name='level43'),
    url(r'leveldd', 'kids.views.level44', name='level44'),
    url(r'levelde', 'kids.views.level45', name='level45'),



    # url(r'^kidsapp/', include('kidsapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
