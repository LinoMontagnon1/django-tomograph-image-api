from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Exame
from .serializers import ExameSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def exame_list(request):
    if request.method == 'GET':
        exames = Exame.objects.all()
        serializer = ExameSerializer(exames, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
