from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('houses/', views.HouseList.as_view()),
    path('houses/<int:pk>/', views.HouseDetail.as_view()),
    path('rooms/', views.RoomList.as_view()),
    path('rooms/<int:pk>/', views.RoomDetail.as_view()),
    path('userdata/<int:pk>/', views.UserHouseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
