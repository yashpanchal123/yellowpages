from django.http import HttpResponse
from .models import Yellow
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from .serializers import YellowSerializer
from rest_framework.permissions import IsAuthenticated  
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination


def home(request):
    return HttpResponse('Api for Yellowpages.')

class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        email = [user.email for user in User.objects.all()]
        return Response(email)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    

class CreateSuperuserView(APIView):
    def post(self, request, format=None):

        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User with this username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )

        token, created = Token.objects.get_or_create(user=user)

        return Response({'message': 'Superuser created successfully.', 'token': token.key}, status=status.HTTP_201_CREATED)


class MPN(LimitOffsetPagination):
    default_limit = 30
    limit_query_param = 20
    max_limit = 50
    offset_query_param = 'p'


class yellowpages_lists(ListCreateAPIView):
    queryset = Yellow.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = YellowSerializer
    pagination_class = MPN
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'ADDRESS', 'CFM_ID', 'CITY', 'COMPANY', 'CONTACT_1','CONTACT_2',
                        'FAX', 'INDUSTRY', 'PHONE', 'STATE', 'ZIP', 'ACCOUNT_ID', 'CATEGORY',
                        'PREFERRED', 'EMAIL', 'WEBSITE', 'URL','SOURCE','SCRAPED_TIME']


class RUD(RetrieveUpdateDestroyAPIView):
    queryset = Yellow.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = YellowSerializer
    pagination_class = MPN
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'ADDRESS', 'CFM_ID', 'CITY', 'COMPANY', 'CONTACT_1','CONTACT_2',
                        'FAX', 'INDUSTRY', 'PHONE', 'STATE', 'ZIP', 'ACCOUNT_ID', 'CATEGORY',
                        'PREFERRED', 'EMAIL', 'WEBSITE', 'URL','SOURCE','SCRAPED_TIME']
