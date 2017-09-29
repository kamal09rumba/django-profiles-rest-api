# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers



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