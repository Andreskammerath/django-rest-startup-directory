from rest_framework.serializers import ModelSerializer
from .models import Post
from organiser.serializers import TagSerializer, StartupSerializer

class PostSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    startup = StartupSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'