from django.contrib import admin
from django.urls import path, include
from api.views import ListUsers, CustomAuthToken

urlpatterns = [
    path('', include('api.urls')),
    path('api/users/', ListUsers.as_view()), # This is for how many user are created.
    path('api/token/auth/', CustomAuthToken.as_view()), # you can check the token of the user by entering the username and password in body.
    path('admin/', admin.site.urls)
]
