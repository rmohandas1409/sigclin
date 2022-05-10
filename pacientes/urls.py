from django.conf.urls import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from .views import LaudoView, exames_new, exames_edit

urlpatterns = [
    path('laudo/<int:id>/', LaudoView.as_view(), name='laudo'),
    path('exames/<int:pk>/', exames_new, name='exames_new'),
    path('exames/new/', exames_new, name='exames_new'),
    path('exames/<int:pk>/edit/', exames_edit, name='exames_edit'),


]
