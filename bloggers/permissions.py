# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission

class AuthorPermission(BasePermission):


    def has_permission(self, request, view):
        """
        Define si el usuario puede ejecutar una acción (GET, POST, PUT, DELETE) sobre la vista `view`
        """

        from bloggers.api import AuthorAPI

        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == "GET" and isinstance(view, AuthorAPI):
            return True

        if request.user.is_authenticated and (request.method == "PUT" or request.method == "DELETE"):
            return True

    def has_object_permission(self, request, view, obj):
        """
        El usuario autenticado (request.user) solo puede trabajar con el usuario solicitado (obj) si es él mismo o es un admin
        """
        return request.user == obj or request.user.is_superuser
