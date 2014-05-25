from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sakhteman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^asli/$','myapp.views.asli',name='asli'),
    url(r'^father/$','myapp.views.father',name='father'),
    url(r'^call/$','myapp.views.call',name='call'),
    url(r'^signin/$','myapp.views.signin',name='signin'),
    url(r'^sabtenam/$','myapp.views.sabtenam',name='sabtenam'),
    url(r'^payment/$','myapp.views.payment',name='payment'),
    url(r'^news/$','myapp.views.news',name='news'),
    url(r'^information/$','myapp.views.information',name='information'),
)
