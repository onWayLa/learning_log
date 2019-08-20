"""定义learning_logs的url模式"""

from django.conf.urls import url
from . import views
from django.urls import re_path

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    # url(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic,name='topic'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # url(r'topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
    # 用于添加新的主题网页
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]
