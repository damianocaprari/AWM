from .serializers import CharacterClassSerializer
from .serializers import SpellSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from app_spells.models import Spell
from app_characterclasses.models import CharacterClass
from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'characterclasses': reverse('api:characterclass-list', request=request, format=format),
#         'users': reverse('api:user-list', request=request, format=format),
#         'spells': reverse('api:spell-list', request=request, format=format)
#     })
#
#
# class CharacterClassList(generics.ListCreateAPIView):
#     permission_classes = (
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#     )
#     queryset = CharacterClass.objects.all()
#     serializer_class = CharacterClassSerializer
#
#
# class CharacterClassDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#     )
#     queryset = CharacterClass.objects.all()
#     serializer_class = CharacterClassSerializer
#
#
#
# class SpellList(generics.ListCreateAPIView):
#     permission_classes = (
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#     )
#     queryset = Spell.objects.all()
#     serializer_class = SpellSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class SpellDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#     )
#     queryset = Spell.objects.all()
#     serializer_class = SpellSerializer
#
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class SpellView(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer

class CharacterClassView(viewsets.ModelViewSet):
    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer