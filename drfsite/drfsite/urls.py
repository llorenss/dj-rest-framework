"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from women.views import WomenViewSet

from rest_framework import routers


# router = routers.SimpleRouter()
# SimpleRouter убирает из адреса api/v1/, а DefaultRouter оставляет
router = routers.DefaultRouter()
router.register(r'women', WomenViewSet, basename='women')
# router.register(r'women', WomenViewSet)
print(router.urls)


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # # после <int:pk> обязательно ставим /, иначе не работает
    # path('api/v1/womenlist/<int:pk>/',
    #      WomenViewSet.as_view({'put': 'update'})),

    # ниже рациональный аналог
    # include(router.urls) - включаем все маршруты, находящиеся в коллекции router
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/
]

# префикс women (women-list, women-detail) наследуется из названия модели,
# from women.views import WomenViewSet
# а не из router.register(r'women', WomenViewSet)

# router.register(r'women', WomenViewSet, basename='new_women')

# basename='new_women' = кс women (women-list, women-detail)
# мы без basename переназначаем именно префикс.
# basename - обязателен, если во вью нет атрибута queryset = ...

# router.register(r'women', WomenViewSet) - здесь начала моршрута, любое слово
# назначаем именно на странице урлов