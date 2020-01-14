from django.contrib import admin
from django.urls import path
from .views import WineViewSet, ReviewViewSet
from rest_framework.authtoken import views

urlpatterns = [
    path('wine/',WineViewSet.as_view(), name='api-wine'),
    path('review/',ReviewViewSet.as_view(), name='api-review'),

]