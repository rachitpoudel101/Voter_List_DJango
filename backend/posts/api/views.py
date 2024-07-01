from rest_framework.viewsets import ModelViewSet
from ..models import *
from .serializers import *

class PostViewSet(ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer

