from rest_framework import viewsets, status
from apps.carreras.models import *
from apps.carreras.api.serializers.serializer import *
from rest_framework.response import Response
from rest_framework.settings import api_settings


class GenericViewSet(viewsets.GenericViewSet):
    model = None
    serializer_class = None

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all().order_by(self.id)
        return self.get_serializer().Meta.model.objects.filter(pk=pk).order_by(self.id).first()


    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        instance = self.get_queryset(pk)
        if instance is not None:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'error':f'No existe un objeto con id={pk}'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset(pk) 

        if instance is not None:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response({'error':f'No existe un objeto con id={pk}'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_queryset(pk)
        if instance is not None:
            instance.delete()
            return Response({'message':f'{self.model.__name__} eliminado correctamente!'},status=status.HTTP_204_NO_CONTENT)
        return Response({'error':f'No existe un objeto con id={pk}'}, status=status.HTTP_404_NOT_FOUND)




















