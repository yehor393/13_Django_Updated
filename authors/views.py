from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Authors
from .serializers import AuthorsSerializer

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_authors(request):
    # name_filter = request.GET.get("name")
    # if name_filter:
    #     queryset = Authors.objects.filter(name__icontains=name_filter)
    # else:
    #     queryset = Authors.objects.all()

    # serializer = AuthorsSerializer(queryset, many=True)
    # return Response(serializer.data)
    return Response({'massage': 'Hello world'})