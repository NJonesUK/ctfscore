from django.conf.urls import patterns, include, url
import users.views
import challenges.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/*/', users.views.profile),
    url(r'^accounts/profile', users.views.profile),
    url(r'^leaderboard', challenges.views.leaderboard),
    url(r'^challenge/(?P<challenge_id>\d+)/$', challenges.views.challenge, name='detail'),
    url(r'^$', users.views.index),

)
