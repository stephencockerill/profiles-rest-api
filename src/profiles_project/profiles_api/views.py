from django.shortcuts import render
from rest_framework.views import (
  APIView,
  Response,
)

# View is the application logic behind the api

class HelloApiView(APIView):
  """
  Test APIView.
  """
  def get(self, request, format=None):
    """
    Returns a list of APIView features.
    """
    an_apiview = [
      'Uses HTTP methods as function (get, post, patch, put, delete)',
      'It is similar to a traditional django view',
      'Gives you the most control over your logic',
      'Is mapped manually to URLs',
    ]

    return Response({'message':'Howdy!', 'an_apiview': an_apiview})
