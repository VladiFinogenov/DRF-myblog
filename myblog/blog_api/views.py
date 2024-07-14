from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog_api.permissions import IsAuthorOrAdmin
from blog_api.models import Post
from blog_api.serializer import PostSerializer


class PostListCreate(APIView):
    """
    Представление для получения списка записей блога и создания новой записи.
    """

    permission_classes = [IsAuthorOrAdmin]

    def get(self, request, format=None):
        """
        Возвращает список всех записей блога.
        """

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Создает новую запись блога.
        """

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Представление для редактирования, и удаления записи блога.
    """

    permission_classes = [IsAuthorOrAdmin]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Возвращает запись блога.
        """

        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Обновляет запись блога.
        """

        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """
        Обновляет поле в записи блога.
        """

        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post,
                                    data=request.data,
                                    partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Удаляет запись блога.
        """

        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
