from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=60, default='NA')
    lastname = models.CharField(max_length=60, default='NA')
    email = models.CharField(max_length=60, default='NA')

    def __str__(self):
        return self.firstname + " " + self.lastname

class House(models.Model):
    houseType = models.CharField(max_length=60, default='NA')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.houseType

class Room(models.Model):
    roomType = models.CharField(max_length=60, default='NA')
    roomPlacementNumber = models.IntegerField()
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house')

    def __str__(self):
        return self.roomType
