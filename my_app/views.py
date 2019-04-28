from django.shortcuts import render, render_to_response
import json
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
def home(request):
    if Blr_FanOnOffStatus.objects.count() > 0:
        blrfanstatus = Blr_FanOnOffStatus.objects.order_by('timestamp').last().status == 1 and "ON" or "OFF"
    else:
        blrfanstatus = None
    return render(request, 'my_app/dashboard.html', {
                                                     'blrfanstatus' : blrfanstatus,
                                                     'sensor1':Sensor1.objects.order_by('timestamp').last(),
                                                     'sensor2':Sensor2.objects.order_by('timestamp').last(),
                                                     'sensor3':Sensor3.objects.order_by('timestamp').last(),
                                                    })

def getsensordata(request):

    if request.method == 'GET':
        data = {
            'valuesensor1': Sensor1.objects.order_by('timestamp').last().value,
            'namesensor1' : Sensor1.objects.order_by('timestamp').last().name,
            'valuesensor2': Sensor2.objects.order_by('timestamp').last().value,
            'namesensor2': Sensor2.objects.order_by('timestamp').last().name,
            'valuesensor3': Sensor3.objects.order_by('timestamp').last().value,
            'namesensor3': Sensor3.objects.order_by('timestamp').last().name,

        }
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(['POST'])
def uploadsensordata(request):
    if request.body:
        data = json.loads(request.body.decode('utf-8'))
        if 'Sensor1' in data:
            obj = Sensor1(name = data['Sensor1']['name'], value=data['Sensor1']['Value'], timestamp=data['time_stamp'], description=data['Sensor1']['Desc'])
            obj.save()
        if 'Sensor2' in data:
            obj = Sensor2(name=data['Sensor2']['name'], value=data['Sensor2']['Value'], timestamp=data['time_stamp'],
                          description=data['Sensor2']['Desc'])
            obj.save()
        if 'Sensor3' in data:
            obj = Sensor3(name=data['Sensor3']['name'], value=data['Sensor3']['Value'], timestamp=data['time_stamp'],
                          description=data['Sensor3']['Desc'])
            obj.save()
        if 'Sensor4' in data:
            obj = Sensor4(name=data['Sensor4']['name'], value=data['Sensor4']['Value'], timestamp=data['time_stamp'],
                          description=data['Sensor4']['Desc'])
            obj.save()
        if 'Sensor5' in data:
            obj = Sensor5(name=data['Sensor5']['name'], value=data['Sensor5']['Value'], timestamp=data['time_stamp'],
                          description=data['Sensor5']['Desc'])
            obj.save()
        if 'Sensor6' in data:
            obj = Sensor6(name=data['Sensor6']['name'], value=data['Sensor6']['Value'], timestamp=data['time_stamp'],
                          description=data['Sensor6']['Desc'])
            obj.save()
        print(data)
        info = {'response': 'accept-data', 'status': '200'}
    else:
        info = {'response': 'No data found', 'status': '400'}
    return HttpResponse(json.dumps(info))


def blrfanstatus(request, status):
    data = {
        'is_valid': False
    }

    if request.is_ajax():
        obj = Blr_FanOnOffStatus(status=status)
        obj.save()
        data.update(is_valid=True)
        data.update(control='blrfan')
        if status == 1:
            data.update(response='ON')
        else:
            data.update(response='OFF')

    return JsonResponse(data)
#
# def blrlightstatus(request,id):
#     if id == 1:
#         obj = Blr_LightOnOffStatus(status=1)
#     elif id == 0:
#         obj = Blr_LightOnOffStatus(status=0)
#     else:
#         return Http404
#
#     obj.save()
#     return render(request, 'my_app/dashboard.html',
#                   {'blrlightstatus': id, })
#
# def vancfanstatus(request,id):
#     if id == 1:
#         obj = Vanc_FanOnOffStatus(status=1)
#     elif id == 0:
#         obj = Blr_LightOnOffStatus(status=0)
#     else:
#         return Http404
#
#     obj.save()
#     return render(request, 'my_app/dashboard.html',
#                   {'vancfanstatus': id, })
#
#
# def vanclightstatus(request,id):
#     if id == 1:
#         obj = Vanc_LightOnOffStatus(status=1)
#     elif id == 0:
#         obj = Blr_LightOnOffStatus(status=0)
#     else:
#         return Http404
#
#     obj.save()
#     return render(request, 'my_app/dashboard.html',
#                   {'vanclightstatus': id, })
#
#
#
