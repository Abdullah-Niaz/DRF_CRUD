from django.shortcuts import render
from .models import *
from rest_framework.response import Response, JSONResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


@api_view()
# Fucntion Based API View
def get_transaction(request):
    queryset = Transcations.objects.all()
    serializer = TransactionSerializer(queryset, many=True)
    return Response({
        "data": serializer.data
    }
    )


# Class Based API View
class TransactionAPI(APIView):
    def get(self, request):
        return Response({
            "message": "This is a GET request",
        })

    def put(self, request):
        return Response({
            "message": "This is a PUT request",
        })

    def post(self, request):
        return Response({
            "message": "This is a POST request",
        })

    def patch(self, request):
        return Response({
            "message": "This is a PATCH request",
        })

    def delete(self, request):
        return Response({
            "message": "This is a DELETE request",
        })
