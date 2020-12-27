from django.contrib import admin
from django.urls import path
from.views import hellowolrdview

urlpatterns = [
    path('',hellowolrdview)
]
