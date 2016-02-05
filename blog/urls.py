from django.conf.urls import url, include
from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    url(r'^posts/new/$', views.post_new, name='post_new'),
    url(r'^posts/edit/(?P<pk>\d+)$', views.post_edit, name='post_new'),
    url(r'^posts/comments/new/(?P<post_pk>\d+)$', views.comment_new, name='comment_new'),
    url(r'^posts/comments/edit/(?P<post_pk>\d+)/(?P<pk>\d+)$', views.comment_edit, name='comment_edit'),

    url(r'^api/v1/', include('blog.api.v1', namespace='api_v1')),
]