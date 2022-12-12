from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import ReviewList, ReviewDetail, Board

urlpatterns = [
    path('review/<int:pk>/', ReviewDetail.as_view()),
    path('review/', ReviewList.as_view()),
    path('board/', Board.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
