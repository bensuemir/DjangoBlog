from rest_framework import status
from rest_framework.response import Response
from blog.models import Post
from blog.api.serializers import PostSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class PostListCreateAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)
    
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




"""
@api_view(['GET', 'POST'])
def post_list_create_api_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""



"""
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_api_view(request, pk):
    try:
        post_instance = Post.objects.get(pk=pk) #PrimeryKey
    except Post.DoesNotExist:
        return Response(
            {
                'errors' : {
                    'code': 404,
                    'message': 'There is no such post with this id ({pk})'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = PostSerializer(post_instance)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post_instance.delete()
        return Response(
            {
                'islem': {
                    'code': 204,
                    'message': f'Post with id ({pk}) has been deleted'
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )
"""  
