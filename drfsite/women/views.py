from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
from .models import Women
from .serializers import WomenSerializer
# from rest_framework import mixins

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # Полезно:
    # Можно убать один из миксинов и сократить функции
    # ModelViewSet = mixins.CreateModelMixin,
    #                mixins.RetrieveModelMixin,
    #                mixins.UpdateModelMixin,
    #                mixins.DestroyModelMixin,
    #                mixins.ListModelMixin,
    #                GenericViewSet

    # Например, изменили фунционал, удалили дестрой (не будет удялять
    # class WomenViewSet(mixins.CreateModelMixin,
    #                mixins.RetrieveModelMixin,
    #                mixins.UpdateModelMixin,
    ##                mixins.DestroyModelMixin,
    #                mixins.ListModelMixin,
    #                GenericViewSet):



