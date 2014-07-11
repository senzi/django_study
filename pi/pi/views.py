# coding=utf-8
from django.http import HttpResponse

import datetime
import os
import sys
import commands
import string

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
    pass

def hello(request):
    return HttpResponse('Welcome to my pi site')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>现在北京时间是 %s.</body></html>" % now
    return HttpResponse(html)

def getCPUtemperature(request):
    res = os.popen('vcgencmd measure_temp').readline()
    CPUtemperature = res.replace("temp=","").replace("'C\n","")
    html = "<html><body>现在CPU的温度是 %s 摄氏度.</body></html>" % CPUtemperature
    return HttpResponse(html)


def check_cpu(request, temperature):

    res = os.popen('vcgencmd measure_temp').readline()
    CPUtemperature = res.replace("temp=","").replace("'C\n","")

    if  float(CPUtemperature) > float(temperature) :
        html = "<html><body>现在CPU的温度大于 %s 摄氏度.</body></html>" % temperature
    else :
        html = "<html><body>现在CPU的温度小于 %s 摄氏度.</body></html>" % temperature
    return HttpResponse(html)

def check_year(request,year):
    try:
        year = int(year)
    except ValueError:
        html = "<html><body>别乱玩,请输入一个数字(年份)<html><body>"
        return HttpResponse(html)
    if int(year) % 4 == 0  and int(year) % 100 != 0 :
        html = "<html><body>%s年是闰年,感觉萌萌哒!<html><body>" % year
    elif int(year) %400 == 0:
        html = "<html><body>%s年是闰年,感觉萌萌哒!<html><body>" % year
    else :
        html = "<html><body>%s年不是闰年,快吃药!<html><body>" % year
    return HttpResponse(html)

























