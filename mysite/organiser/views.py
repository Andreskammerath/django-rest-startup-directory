from django.shortcuts import(
    get_list_or_404,
    get_object_or_404
)
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from organiser.serializers import TagSerializer, StartupSerializer, NewsLinkSerializer
from organiser.models import Tag, Startup, NewsLink

class TagAPIDetail(generics.RetrieveAPIView):
    'Return JSON for single Tag Object'

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class TagAPIList(generics.ListAPIView):
    'Return JSON for List Tag Object'

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StartupAPIDetail(generics.RetrieveAPIView):
    'Return JSON for single Tag Object'

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = 'slug'


class StartupAPIList(generics.ListAPIView):
    'Return JSON for List Tag Object'

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class NewsLinkAPIDetail(generics.RetrieveAPIView):
    'Return JSON for single Tag Object'

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
    lookup_field = 'slug'


class NewsLinkAPIList(generics.ListAPIView):
    'Return JSON for List Tag Object'

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer