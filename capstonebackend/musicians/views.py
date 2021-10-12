from rest_framework import status
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

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_musicians(request):

    print('User', f"{request.user.id}")

    if request.method == 'POST':
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        musicians = Musician.objects.filter(user_id=request.user.id)
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)