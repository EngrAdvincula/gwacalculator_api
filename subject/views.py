from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json


from subject.models import SubList

# Create your views here.

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_subject(request, subject_name):
    if request.method == 'GET':
        try:
            subject = SubList.objects.get(name=subject_name)
            response = json.dumps([{ 'Subject': subject.name, 'Unit': subject.units}])
        except:
            response = json.dumps([{ 'Error': 'No subject with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_subject(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        subject_name = payload['subject_name']
        units = payload['units']
        subject = SubList(name=subject_name, units=units)
        try:
            subject.save()
            response = json.dumps([{ 'Success': 'Subject added successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'Subject could not be added!'}])
    return HttpResponse(response, content_type='text/json')