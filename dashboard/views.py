from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.http import HttpResponse
from nginx.views import *
import json
import time

@login_required(login_url="/login/")
def view(request):
    _sysinfo = get_sysinfo()
    return render_to_response('dashboard/view.html',{'sysinfo' : _sysinfo})

@login_required(login_url="/login/")
def get_status_info(request):
    content = {
        'flag':"Success",
        'content':get_statusinfo()
    }
    return HttpResponse(json.dumps(content))
