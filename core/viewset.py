from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .userserializer import UserSerializer, User
from django_filters.rest_framework import DjangoFilterBackend

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})

        # and everything else you want to send in the response
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['groups',]