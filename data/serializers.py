from rest_framework import serializers

from .models import User, House, Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('roomType', 'roomPlacementNumber')

class HouseSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True, many=True)

    class Meta:
        model = House
        fields = ('houseType', 'room')

class UserSerializer(serializers.ModelSerializer):
    house = HouseSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname', 'email', 'house')
