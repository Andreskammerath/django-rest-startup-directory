from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from organiser.models import Tag, Startup, NewsLink

class TagSerializer(ModelSerializer):
    
    url = HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='api_tag_detail'
    )

    class Meta:
        model = Tag
        exclude = ('id',)

class StartupSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='api_startup_detail'
    )
    tags = TagSerializer(many=True)

    class Meta:
        model = Startup
        exclude = ('id',)

class NewsLinkSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='api_newslink_detail'
    )
    startup = StartupSerializer()

    class Meta:
        model = NewsLink
        exclude = ('id',)