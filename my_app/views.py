from django.shortcuts import render, render_to_response
import json
from .models import *
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

# Create your views here.
def home(request):

    return render(request, 'my_app/dashboard.html', {'sensor1':Sensor1.objects.order_by('timestamp').last(),
                                                     'sensor2':Sensor2.objects.order_by('timestamp').last(),
                                                     'sensor3':Sensor3.objects.order_by('timestamp').last(),
                                                     'blrfanstatus': Blr_FanOnOffStatus.objects.order_by('timestamp').last().status,
                                                     'blrlightstatus': Blr_FanOnOffStatus.objects.order_by('timestamp').last().status,
                                                     'vancfanstatus': Blr_FanOnOffStatus.objects.order_by('timestamp').last().status,
                                                     'vanclightstatus': Blr_FanOnOffStatus.objects.order_by('timestamp').last().status})

@csrf_exempt
@require_http_methods(['POST'])
def uploadsensordata(request):
    if request.body:
        data = json.loads(request.body.decode('utf-8'))
        obj = Sensor1(name = data['Sensor1']['name'], value=data['Sensor1']['Value'], timestamp=data['time_stamp'], description=data['Sensor1']['Desc'])
        obj.save()
        obj = Sensor2(name=data['Sensor2']['name'], value=data['Sensor2']['Value'], timestamp=data['time_stamp'],
                      description=data['Sensor2']['Desc'])
        obj.save()
        obj = Sensor3(name=data['Sensor3']['name'], value=data['Sensor3']['Value'], timestamp=data['time_stamp'],
                      description=data['Sensor3']['Desc'])
        obj.save()
        print(data)
        info = {'response': 'accept-data', 'status': '200'}
    else:
        info = {'response': 'No data found', 'status': '400'}
    return HttpResponse(json.dumps(info))

def blrfanstatus(request, id):
    if id == 1:
        obj = Blr_FanOnOffStatus(status=1)
    elif id == 0:
        obj = Blr_FanOnOffStatus(status=0)
    else:
        return Http404

    obj.save()
    return render(request, 'my_app/dashboard.html',
                  {'blrfanstatus': id,})

def blrlightstatus(request,id):
    if id == 1:
        obj = Blr_LightOnOffStatus(status=1)
    elif id == 0:
        obj = Blr_LightOnOffStatus(status=0)
    else:
        return Http404

    obj.save()
    return render(request, 'my_app/dashboard.html',
                  {'blrlightstatus': id, })

def vancfanstatus(request,id):
    if id == 1:
        obj = Vanc_FanOnOffStatus(status=1)
    elif id == 0:
        obj = Blr_LightOnOffStatus(status=0)
    else:
        return Http404

    obj.save()
    return render(request, 'my_app/dashboard.html',
                  {'vancfanstatus': id, })


def vanclightstatus(request,id):
    if id == 1:
        obj = Vanc_LightOnOffStatus(status=1)
    elif id == 0:
        obj = Blr_LightOnOffStatus(status=0)
    else:
        return Http404

    obj.save()
    return render(request, 'my_app/dashboard.html',
                  {'vanclightstatus': id, })



