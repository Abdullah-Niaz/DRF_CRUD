from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.


@api_view()
def get_transaction(request):
    queryset = Transcations.objects.all()
    serializer = TransactionSerializer(queryset, many=True)
    return Response({
        "data": serializer.data
    }
    )
