# coding=utf-8
from django.http import HttpResponse

from django.shortcuts import render_to_response
import datetime
import os
import sys
import commands
import string
import RPi.GPIO as GPIO  
import time 

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
    pass

def hello(request):
    return render_to_response('dateapp/home.html', locals())

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('dateapp/time.html', locals())

def getCPUtemperature(request):
    res = os.popen('vcgencmd measure_temp').readline()
    CPUtemperature = res.replace("temp=","").replace("'C\n","")
    return render_to_response('dateapp/temperature.html', locals())


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

  
def ledset(request,ledflag):
    GPIO.setwarnings(False)
    led = 11 
    GPIO.setmode(GPIO.BOARD)  
    # need to set up every channel which are using as an input or an output  
    GPIO.setup(led, GPIO.OUT)
    try:
        ledflag = int(ledflag)
    except ValueError:
        html = "<html><body>别乱玩,请输入0或者1<html><body>"
        return HttpResponse(html)
    if   ledflag == 0 :
        GPIO.output(led, GPIO.LOW)
        html = "<html><body>led灯已经熄灭,感觉萌萌哒<html><body>"
    elif ledflag == 1 :
        html = "<html><body>led灯我帮你点亮啦,记得关灯<html><body>"
        GPIO.output(led, GPIO.HIGH)
    else:
        html = "<html><body>别乱玩,请输入0或者1<html><body>"
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return render_to_response('dateapp/display.html', locals())
 
























