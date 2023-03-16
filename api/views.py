from django.shortcuts import render
from .serializers import ContactFormSerializer , CallBackFormSerializer , NewsLetterSerializer
from main.models import ContactForm , CallBackForm , NewsLetter
from rest_framework import mixins
from rest_framework import viewsets ,status
from rest_framework.response import Response
class ContactFormViewSet (mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = kwargs['pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class CallBackFormViewSet (mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CallBackForm.objects.all()
    serializer_class = CallBackFormSerializer
    def create(self, request, *args, **kwargs):
        request.data['user'] = kwargs['pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class NewsLetterViewSet (mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer
    def create(self, request, *args, **kwargs):
        request.data['user'] = kwargs['pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)