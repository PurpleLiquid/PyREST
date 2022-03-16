from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, HouseSerializer, RoomSerializer
from .models import User, House, Room

factory = APIRequestFactory()
request = factory.get('/')


serializer_context = {
    'request': Request(request),
}

class UserList(APIView):
    def get(self, request, format=None, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(instance=users, context=serializer_context)
        return Response(serializer.data)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HouseList(APIView):
    def get(self, request, format=None, **kwargs):
        houses = House.objects.all()
        serializer = HouseSerializer(instance=houses, context=serializer_context)
        return Response(serializer.data)

class HouseDetail(APIView):
    def get_object(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        house = self.get_object(pk)
        serializer = HouseSerializer(instance=house, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        house = self.get_object(pk)
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        house = self.get_object(pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RoomList(APIView):
    def get(self, request, format=None, **kwargs):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        room = self.get_object(pk)
        serializer = RoomSerializer(instance=room, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        room = self.get_object(pk)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        room = self.get_object(pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserHouseDetail(APIView):
    def get(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        house = House.objects.get(user=user)
        room = Room.objects.filter(house=house)
        userserializer = UserSerializer(instance=user, context=serializer_context)
        houseSerializer = HouseSerializer(instance=house, context=serializer_context)
        roomSerializer = RoomSerializer(instance=room, context=serializer_context, many=True)

        return Response({
            'User': userserializer.data,
            'House': houseSerializer.data,
            'Rooms': roomSerializer.data,
        })

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, *args, **kwargs):
        user = self.get_user(pk)
        house = House.objects.get(user=user)
        rooms = Room.objects.filter(house=house)
        newRoomData = request.data['Rooms']

        i = 0
        for roomData in newRoomData:
            serializer = RoomSerializer(rooms[i], data=newRoomData[i])
            if serializer.is_valid():
                serializer.save()
                i += 1
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        newRooms = Room.objects.filter(house=house)
        serializer = RoomSerializer(newRooms, many=True)
        return Response(serializer.data)
