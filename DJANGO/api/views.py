from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from api.serializers import CodeExplainSerializers


class CodeExplainerView(views.APIView):
    serializer_class = CodeExplainSerializers

    def get(self, request, format=None):
        data = {"message": "Hello, world!"}
        return Response(data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView:
    pass


class UserView:
    pass
