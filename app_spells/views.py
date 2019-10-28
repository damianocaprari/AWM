from app_spells.models import Spell, SpellTag, SpellAdditionalInfo, SpellCA
from app_spells.serializers import SpellSerializer, SpellCASerializer, SpellTagSerializer, SpellAdditionalInfoSerializer
from rest_framework import viewsets, permissions


class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    permission_classes = (permissions.AllowAny,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)


class SpellTagViewSet(viewsets.ModelViewSet):
    queryset = SpellTag.objects.all()
    serializer_class = SpellTagSerializer
    permission_classes = (permissions.AllowAny,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)


class SpellAdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = SpellAdditionalInfo.objects.all()
    serializer_class = SpellAdditionalInfoSerializer
    permission_classes = (permissions.AllowAny,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)


class SpellCAViewSet(viewsets.ModelViewSet):
    queryset = SpellCA.objects.all()
    serializer_class = SpellCASerializer
    permission_classes = (permissions.AllowAny,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)
