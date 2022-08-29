import json
from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time

from chat.models import RoomMember, ChatRoom, RoomAgenda
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def getToken(request):
    appId = 'ebeebb6018f249da8f9a1e84668032a1'
    appCertificate = '7de620c68e184f5ca61e6e23ec2c27f4'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    #Build token with uid
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid}, safe=False)

def Home(request):
    return render(request, 'pages/front.html')

def Create(request):
    return render(request, 'pages/create.html')

def Join(request):
    return render(request, 'pages/join.html')

def Room(request):
    return render(request, 'pages/room.html')

@csrf_exempt
def newMeeting(request):
    data = json.loads(request.body)

    room, crated = ChatRoom.objects.get_or_create(name=data['room_name'], meeting_duration=data['duration'])

    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room=room
    )

    return JsonResponse({'name':data['name']}, safe=False)

@csrf_exempt
def joinMeeting(request):
    data = json.loads(request.body)

    room = ChatRoom.objects.get(name=data['room_name'])

    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room=room
    )

    return JsonResponse({'name':data['name']}, safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    room = ChatRoom.objects.get(name=room_name)
    
    member = RoomMember.objects.get(
        uid = uid,
        room = room,
    )
    name = member.name
    print(name)
    return JsonResponse({'name': name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    
    room = ChatRoom.objects.get(name = data['room_name'])
    
    member = RoomMember.objects.get(
        uid = data['UID'],
        name = data['name'],
        room = room,
    )
    member.delete()
    return JsonResponse('Member was deleted', safe=False)

def Agenda(request):
    return render(request, 'pages/agenda.html')

def addAgenda(request):
    pass
