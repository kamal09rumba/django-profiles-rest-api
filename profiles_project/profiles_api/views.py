# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions




# http status http 404,http 405

class HelloApiView(APIView):
    """ test apiview"""
    # docstring

    serializer_class = serializers.HelloSerializer
    # important to generate input field

    def get(self, response, format=None):
        """ Returns list of apiviews features """
        an_apiview = [
            'HTTP metho as function get, post, put, patch, delete',
            'it is similar to traditional django view',
            'gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello!', 'api_view': an_apiview})


    def post(self , request):
        """ create a hello message with our name """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name    = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self , request , pk=None):
        """ Handles updateing an object """
        return Response({'method':'put'})

    def patch(self , request , pk=None):
        """ patch request, only updates field provides in the request """
        return Response({'message':'patch'})

    def delete(self , request , pk=None):
        """ deletes an object """
        return Response({'message':'delete'})




class HelloViewSet(viewsets.ViewSet):
    """" Test api viewsets """

    serializer_class = serializers.HelloSerializer

    def list(self , request):
        """ returns hello message """
        a_viewsets = [
                    'user action (list, create, retrive, updat, partial update, destroy)',
                    'automatically maps to URLs using router',
                    'provides more functionality with less code'
                ]
        return Response({'message': 'Hello from viewsets','a_viewsets':a_viewsets})

    def create(self, request):
        """" create a new hello messsage """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name    = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """" handles getting an object by its object """
        return Response({'http_metho':'GET'})

    def update(self , request , pk=None):
        """ handles updateing of an object  """
        return Response({'http_method':'PUT'})

    def partial_update(self , request , pk=None):
        """ handles updating part of object """
        return Response({'http_method':'PATCH'})

    def destroy(self , request , pk=None):
        """ handles removing of object """
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating and updating the profiles """

    serializer_class        = serializers.UserProfileSerializer
    queryset                = models.UserProfile.objects.all()
    authentication_classes  = (TokenAuthentication,)
    permission_classes      = (permissions.UpdateOwnProfile,)