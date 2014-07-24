from django.conf.urls import patterns, url

from apps.polls import views

urlpatterns = patterns('',
	# ex: /polls/
		url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /polls/5
		url(r'^(?P<poll_id>\d+)/$', views.DetailView.as_view(), name='detail'),
	# ex: /polls/5/results/
		url(r'^(?P<poll_id>\d+)/results/$', views.detail, name='results'),
	# ex: /polls/5/vote/
		url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	)