from django.contrib import admin
from .models import User, House, Room

class RoomAdminInline(admin.TabularInline):
    model = Room
    extra = 4
    fields = ['roomType', 'roomPlacementNumber']

class HouseAdmin(admin.ModelAdmin):
    list_display = ['houseType']
    inlines = [RoomAdminInline]

class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Room)
