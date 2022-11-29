from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoticeSerializer
from .models import Notice

class NoticeView(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all().order_by('-createdTime')
