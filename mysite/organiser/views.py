from django.shortcuts import(
    get_list_or_404,
    get_object_or_404
)
from django.views import View
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from organiser.serializers import TagSerializer
from organiser.models import Tag

class TagAPIDetail(APIView):
    'Return JSON for single Tag Object'

    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = TagSerializer(tag, context={'request': request})
        return Response(s_tag.data)


class TagAPIList(APIView):
    'Return JSON for List Tag Object'

    def get(self, request):
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(tag_list, context={'request': request}, many=True)
        return Response(s_tag.data)
