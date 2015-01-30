from rest_framework import viewsets
from TLKrest.serializers import *
from TLKdb.models import *


# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    """
    Derp Derp Derpity Derp [Herp][ref]

    [ref]: http://derp.derp.fi/derp
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberAddViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberAddSerializer

class MemberTypeViewSet(viewsets.ModelViewSet):
    queryset = MemberType.objects.all()
    serializer_class = MemberTypeSerializer
