# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models.boardlist import BoardList
from .serializers import ReviewSerializer, BoardSerializer
from drfproject.models.models import Review

class BoardDelete(APIView):
    def delete(self, request, board_id):
        print('delete')
        board = BoardList.objects.get(pk=board_id)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Board(APIView):
    def post(self, request):
        print('here is the post')
        serializer = BoardSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        boards = BoardList.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)


class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('post')
        serializer = ReviewSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print(1)
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


