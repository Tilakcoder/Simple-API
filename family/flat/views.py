from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Member, Parent, Children
from .serializers import MemberSerializer, ParentSerializer, ChildrenSerializer
from rest_framework import generics


class MemberListView(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class ParentListView(generics.ListCreateAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


class ChildrenListView(generics.ListCreateAPIView):
    serializer_class = ChildrenSerializer
    queryset = Children.objects.all()
