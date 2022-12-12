from django.contrib import admin

from drfproject.models.boardlist import BoardList
from drfproject.models.models import Review

# Register your models here.

admin.site.register(Review)
admin.site.register(BoardList)