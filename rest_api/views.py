from django.shortcuts import render
from core.models import Thread, Comentario
from .serializers import ThreadSerializer, ComentarioSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def vista_thread(request):
    if request.method == 'GET':
        threads = Thread.objects.all()
        serializer = ThreadSerializer(threads, many=True)


        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ThreadSerializer(data = data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def modificar_thread(request, id):
    try:
        thread = Thread.objects.get(thread_id=id)
    except Thread.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ThreadSerializer(thread)

        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = ThreadSerializer(thread, data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        thread.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    



@csrf_exempt
@api_view(['GET', 'POST'])
def vista_comentario(request):
    if request.method == 'GET':
        comentario = Comentario.objects.all()
        serializer = ComentarioSerializer(comentario, many=True)


        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComentarioSerializer(data = data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def modificar_comentario(request, id):
    try:
        comentario = Comentario.objects.get(comentario_id=id)
    except Comentario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ComentarioSerializer(comentario)

        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = ComentarioSerializer(comentario, data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        comentario.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)