"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from api.views import BillViewSet, BillSummaryViewSet, BillInfoViewSet


router = routers.DefaultRouter()
router.register(r'bills', BillViewSet, basename='bill')
router.register(r'bill-summary', BillSummaryViewSet, basename='billSummary')
router.register(r'bill-info', BillInfoViewSet, basename='billInfo')

urlpatterns = [
    path('xadmin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi', get_schema_view(
        title="Bookkeeping Demo",
        description="API for bookkeeping project",
        version="1.0.0"
    ), name='openapi-schema')
]

urlpatterns += staticfiles_urlpatterns()
