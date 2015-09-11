from django.conf.urls import *
from workflow.views import *

urlpatterns = patterns('',
    (r'^$', list_workorder),
    (r'^list/$', list_workorder),
    (r'^task/(?P<id>[^/]+)/$', task_workorder),
    (r'^approval/$', approval_workorder),
    # (r'add/$', add_cmdb),

    # (r'view/(?P<id>[^/]+)/$', view_cmdb),
    # (r'del/(?P<id>[^/]+)/$', del_cmdb),
)