from django.conf.urls.defaults import *
from website.views import HomePage, AboutMe
from blog.views import Blog, Article, CodeAndData, ProjectContent, ResearchContent

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^testing/', include('testing.foo.urls')),
    url(r'^$', HomePage),
    url(r'about$', AboutMe),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    url(r'blog$', Blog),
    url(r'blog/post_num/(.*)$', Article),
    url(r'research$', ResearchContent),
    url(r'code$', CodeAndData),
    url(r'projects$', ProjectContent),
)
