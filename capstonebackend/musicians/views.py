from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Musician
from .serializers import MusicianSerializer
from django.contrib.auth.models import User


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_musicians(request):
    if request.method == 'POST':
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_204_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)