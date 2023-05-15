from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    DestroyAPIView, UpdateAPIView, CreateAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Books
from .serializers import BookSerializer
from rest_framework.views import APIView


# class BookListApiView(ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
class BookListApiView(APIView):

    def get(self, request):
        books = Books.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data
        }
        return Response(data)


# class BookCreateApiView(CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
class BookCreateApiView(APIView):

    def post(self, request):
        data = request.date
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'satatus': 'Books are saved to the database',
                'books': data
            }
            return Response(data)
        else:
            return Response(
                {
                    'status': False,
                    'message': 'Serializer is not valid'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class BookListCreateApiView(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


# class BookDetailApiView(RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'satatus': 'Successfull',
                'books': serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    'status': 'Does not exists',
                    'message': 'Book is not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


# class BookUpdateApiView(UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Books.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response (
                {
                    'status': True,
                    'Message': f"Book {book_saved} updated successfully"
                }
            )


# class BookDeleteApiView(DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    'status': True,
                    'Message': 'Successfully deleted'
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    'status': False,
                    'Message': 'Book is not found'
                }, status=status.HTTP_404_NOT_FOUND
            )


class BookDetailUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


