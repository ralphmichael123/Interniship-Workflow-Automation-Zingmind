import imp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from account.models import account
from account.serializers import RegistrationSerializers

# Create your views here.


@csrf_exempt
def registrationapi(request,id=0):
    if request.method=='GET':
        registration = account.objects.all()
        registrationserializer = RegistrationSerializers(registration,many=True)
        return JsonResponse(registrationserializer.data,safe=False)
    elif request.method=='POST':
        registration_data=JSONParser().parse(request)
        registration_serializer=RegistrationSerializers(data=registration_data)
        if registration_serializer.is_valid():
            registration_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        registration_data=JSONParser().parse(request)
        registrations=registration.objects.get(RegistrationId=registration_data['RegistrationId'])
        registration_serializer=RegistrationSerializers(registrations,data=registration_data)
        if registration_serializer.is_valid():
            registration_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse("Failed too Update")
    elif request.method=='DELETE':
        registrations=registrations.objects.get(RegistrationId=id)
        registrations.delete()
        return JsonResponse("Deleted Successfully", safe=False)
