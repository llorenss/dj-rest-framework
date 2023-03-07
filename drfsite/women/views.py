from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
from rest_framework.response import Response

from .models import Women, Category
from .serializers import WomenSerializer
# from rest_framework import mixins
from rest_framework.decorators import action


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        # http://127.0.0.1:8000/api/v1/women/
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        # http://127.0.0.1:8000/api/v1/women/2/
        return Women.objects.filter(pk=pk)
        # возвращаем первые 3 записи
        # обязательно в basename='women'

    # декоратор @action() добавляет маршруты, если нам
    # не хватает вложенных путей и данных из вью
    # http://127.0.0.1:8000/api/v1/women/category/

    # @action(methods=['get'], detail=False)
    # def category(self, request):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})
    #     # новый маршрут формируется используя имя метода
    #     # category из  def category(self, request):
    #     # [c.name for c in cats] - фактически создаём список
    #     # итерируем в квадратных скобках

    # ниже возможно выбрать уже одну конкретную категорию.
    # особенность: ставим айди перед категорией
    # http://127.0.0.1:8000/api/v1/women/2/category/
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
        # новый маршрут формируется используя имя метода
        # category из  def category(self, request):



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
