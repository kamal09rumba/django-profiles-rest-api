# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ test apiview"""
    # docstring
    def get(self, response, format=None):
        """ Returns list of apiviews features """
        an_apiview = [
            'HTTP metho as function get, post, put, patch, delete',
            'it is similar to traditional django view',
            'gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello!', 'api_view': an_apiview})