from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from authentication.serializers import RegistrationSerializer
from .models import BandRequest, Friends1, Musician
from .serializers import BandRequestSerializer, MusicianSerializer
from django.contrib.auth.models import User
from rest_framework import serializers



# Create your views here.
# class MusicianList(APIView):

#     permission_classes = [AllowAny]

#     def get(self, request):
#         musicians = Musician.objects.all()
#         serializer = MusicianSerializer(musicians, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_musicians(request):
    musicians = Musician.objects.all()
    serializer = MusicianSerializer(musicians, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_musician(request):
    user = User.objects.filter(id=request.user.id)
    serializer = RegistrationSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_other_musician(request, pk):
    user = User.objects.filter(pk=pk)
    serializer = RegistrationSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_details(request, pk):
    profile = Musician.objects.filter(pk=pk)
    serializer = MusicianSerializer(profile, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'GET'])
@permission_classes([IsAuthenticated])
def user_profiles(request):

    print('User', f"{request.user.id}")

    if request.method == 'POST':
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        profile = Musician.objects.get(user_id=request.user.id)
        serializer = MusicianSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        musicians = Musician.objects.filter(user_id=request.user.id)
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def friend_request(request, pk):
    sender = request.user
    recipient = User.objects.get(id=pk)
    model = BandRequest.objects.get_or_create(sender=request.user, receiver=recipient)
    serializer = BandRequestSerializer(model, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_request(request, pk):
    client1 = User.objects.get(id=pk)
    if request.method == 'DELETE':
        model1 = BandRequest.objects.get(sender=request.user, receiver=client1)
        serializer = BandRequestSerializer(model1, data=request)
        model1.delete()
    elif request.method == 'DELETE':
        model2 = BandRequest.objects.get(sender=client1, receiver=request.user)
        serializer = BandRequestSerializer(model2, data=request)
        model2.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_or_remove_friend(request, operation, pk):
    new_friend = User.objects.get(id=pk)
    if operation == 'add':
        fq = FriendRequest.objects.get(sender=new_friend, receiver=request.user)
        Friends1.make_friend(request.user, new_friend)
        Friends1.make_friend(new_friend, request.user)
        fq.delete()
    elif operation == 'remove':
        Friends1.lose_friend(request.user, new_friend)
        Friends1.lose_friend(new_friend, request.user)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_friend(request,  pk):
    new_friend = User.objects.get(id=pk)   
    fq = BandRequest.objects.get(sender=new_friend, receiver=request.user)
    Friends1.make_friend(request.user, new_friend)
    Friends1.make_friend(new_friend, request.user)
    fq.delete()
    
    return Response(status=status.HTTP_200_OK)