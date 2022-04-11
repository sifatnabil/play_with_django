from rest_framework.decorators import api_view
from rest_framework.response import Response
from meetups.models import Meetup
from .serializers import MeetupSerializer, RegistrationSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/meetups',
        'GET /api/meetups/:slug'
    ]

    return Response(routes)

@api_view(['GET'])
def getMeetups(request):
    meetups = Meetup.objects.all()
    serializer = MeetupSerializer(meetups, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMeetup(request, id):
    meetup = Meetup.objects.get(id=id)
    serializer = MeetupSerializer(meetup)
    return Response(serializer.data)

@api_view(['POST',])
def registrationView(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        
        return Response(data)