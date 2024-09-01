from django.shortcuts import render
from .models import *
from rest_framework.response import Response
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
        queryset = Transcations.objects.all().order_by("-pk")
        serializer = TransactionSerializer(queryset, many=True)
        return Response({
            "data": serializer.data
        }
        )

    def post(self, request):
        dt = request.data
        queryset = Transcations.objects.all()
        serializer = TransactionSerializer(data=dt)
        if not serializer.is_valid():
            return Response({
                "Message": "Data not save ",
                "errors ": serializer.error_messages,
            })
        serializer.save()
        return Response({
            "message": "Data Saved",
            "Data": serializer.data,
        })

    def put(self, request):
        return Response({
            "message": "This is a PUT request",
        })

    def patch(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message": "Data Not Update",
                "error": "id is required"
            })

        transaction = Transcations.objects.get(id=data.get('id'))
        serializer = TransactionSerializer(
            transaction, data=data, partial=True)
        if not serializer.is_valid():
            return Response({
                "Message": "Data not save ",
                "errors ": serializer.error_messages,
            })
        serializer.save()
        return Response({
            "message": "Data Saved",
            "Data": serializer.data,
        })

    def delete(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message": "Data Not Update",
                "error": "id is required"
            })

        transaction = Transcations.objects.get(id=data.get('id')).delete()
        return Response({
            "message": "Data Deleted",
            "Data": {},
        })
