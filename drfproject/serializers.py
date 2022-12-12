from rest_framework import serializers

from drfproject.models.boardlist import BoardList
from drfproject.models.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'date_created')
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardList
        fields = '__all__'
