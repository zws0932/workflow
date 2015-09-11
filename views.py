#-*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

from workflow.models import *
from workflow.forms import *

def list_workorder(request):
    """工单列表"""
    workorder = Workorder.objects.all()
    paginator = Paginator(workorder ,20)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        workorder = paginator.page(page)
    except :
        workorder = paginator.page(paginator.num_pages)
    pages = workorder.paginator.page_range   # 页码列表

    t = get_template('workflow/list.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


@login_required
def task_workorder(request, id):
    """任务流程"""
    user = request.user
    if request.method == 'POST':#提交请求时才会访问这一段，首次访问页面时不会执行
        form = TaskForm(request.POST or None, request.FILES,)
        if form.is_valid():
            form.save()
            form = TaskForm(initial={ 'type':id, 'creator':user.id, 'state':1})
    else:#首次访问该url时没有post任何表单
        form = TaskForm(initial={ 'type':id, 'creator':user.id, 'state':1}) #第一次生成的form里面内容的格式
    t = get_template('workflow/add.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def approval_workorder(request):
    """审批列表"""
    user = request.user
    approval = Workorder.objects.all()   #filter(type_id='True').order_by('-is_top',"-publish_time")
    paginator = Paginator(approval ,20)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        approval = paginator.page(page)
    except :
        approval = paginator.page(paginator.num_pages)
    pages = approval.paginator.page_range   # 页码列表

    t = get_template('workflow/approval.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
