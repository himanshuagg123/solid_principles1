from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PostSerializer
from .service import PostService

class PostAPI(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = PostService()  

    def get(self, request):
        posts = self.service.get_all_posts()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        post = self.service.create_post(title, content)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
