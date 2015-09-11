#-*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponseForbidden
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
    """任务添加"""
    user = request.user
    if request.method == 'POST':#提交请求时才会访问这一段，首次访问页面时不会执行
        form = TaskForm(request.POST or None, request.FILES,)
        if form.is_valid():
            print '++++++++++++++'
            print form.clean
            if request.POST.has_key('sub'):
                result=form.save(commit=False)
                result.state = 2
                result.save() # 点击提交按钮则改变状态为已提交
            else:
                form.save()
            return HttpResponseRedirect('/workflow/sqlist/')
    else:#首次访问该url时没有post任何表单
        form = TaskForm(initial={ 'type':id, 'creator':user.id, 'state':1}) #第一次生成的form里面内容的格式
    t = get_template('workflow/add.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


@login_required
def edit_workorder(request, id):
    """任务编辑"""
    approval = Task.objects.get(pk=int(id))
    if(int(approval.state) == 0) or (int(approval.state) == 1) or (int(approval.state) == 4):
        if request.method == "POST":
            formset = TaskForm(request.POST or None,request.FILES, instance=approval)
            if formset.is_valid():
                if request.POST.has_key('sub'):
                    Task.objects.filter(id=id).update(state=2)
                else:
                    formset.save()
                return HttpResponseRedirect('/workflow/sqlist/')
        else:
            formset = TaskForm(instance=approval)
    else:
        return HttpResponseForbidden('<h1>403 Forbidden </h1>')
    t = get_template('workflow/edit.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def splist_workorder(request):
    """审批列表"""
    user = request.user
    splist = Task.objects.all().order_by('state')#filter(state=3)
    paginator = Paginator(splist ,20)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        splist = paginator.page(page)
    except :
        splist = paginator.page(paginator.num_pages)
    pages = splist.paginator.page_range   # 页码列表

    t = get_template('workflow/splist.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required
def approval_workorder(request, id):
    """审批处理"""
    approval = Task.objects.get(pk=int(id))
    if request.method == "POST":
        formset = ApprovalForm(request.POST or None,request.FILES, instance=approval)

        print request.POST.get('state')
        print formset

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/workflow/splist/')
    else:
        formset = ApprovalForm(initial={'state':3},instance=approval)
    t = get_template('workflow/approval.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def sqlist_workorder(request):
    """申请列表"""
    user = request.user
    task_sqlist = Task.objects.filter(creator=user.id).order_by('state')
    paginator = Paginator(task_sqlist ,20)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        task_sqlist = paginator.page(page)
    except :
        task_sqlist = paginator.page(paginator.num_pages)
    pages = task_sqlist.paginator.page_range   # 页码列表

    t = get_template('workflow/sqlist.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def cllist_workorder(request):
    """处理列表"""
    user = request.user
    cllist = Task.objects.all().order_by('state')#filter(state=3)
    paginator = Paginator(cllist ,20)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        cllist = paginator.page(page)
    except :
        cllist = paginator.page(paginator.num_pages)
    pages = cllist.paginator.page_range   # 页码列表

    t = get_template('workflow/cllist.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


@login_required
def handle_workorder(request, id):
    """审批处理"""
    handle = Task.objects.filter(pk=int(id))
    if request.method == "POST":
        if request.POST.has_key('handle'):
            handle.update(state=4,feedback=request.POST.get('feedback'))
        if request.POST.has_key('finish'):
            handle.update(state=5)
            return HttpResponseRedirect('/workflow/sqlist/')
        else:
            handle.update(state=0,feedback=request.POST.get('feedback'))
    return HttpResponseRedirect('/workflow/cllist/')