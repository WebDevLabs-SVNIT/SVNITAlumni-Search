from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()
import haystack
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alumni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
	url(r'^search/', include('haystack.urls'))
)
import sys
# ...
def get_sys_path(request):
    return HttpResponse(str(sys.path))