#-*- coding: utf-8 -*-
from django.conf.urls import *
from workflow.views import *

urlpatterns = patterns('',
    (r'^$', list_workorder),
    (r'^list/$', list_workorder),
    (r'^splist/$', splist_workorder),
    (r'^sqlist/$', sqlist_workorder),
    (r'^cllist/$', cllist_workorder),
    (r'^approval/(?P<id>[^/]+)/$', approval_workorder),
    (r'^handle/(?P<id>[^/]+)/$', handle_workorder),
    (r'^finish/(?P<id>[^/]+)/$', handle_workorder),  # 和处理视图共用
    (r'^task/(?P<id>[^/]+)/$', task_workorder),
    (r'^edit/(?P<id>[^/]+)/$', edit_workorder),
    # (r'add/$', add_cmdb),

    # (r'view/(?P<id>[^/]+)/$', view_cmdb),
    # (r'del/(?P<id>[^/]+)/$', del_cmdb),
)