# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


from bloggers.permissions import AuthorPermission
from bloggers.serializers import AuthorListSerializer, AuthorSerializer


class AuthorAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AuthorPermission]

    def get(self, request):
        users = User.objects.all()
        paginator = PageNumberPagination()
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = AuthorListSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AuthorPermission]

    def get(self, request, pk):
        user = get_object_or_404(User, username=pk)
        self.check_object_permissions(request, user)
        serializer = AuthorSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, username=pk)
        self.check_object_permissions(request, user)
        serializer = AuthorSerializer(user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, username=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)