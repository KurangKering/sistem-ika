from django.urls import path

from . import views

urlpatterns = [
    path('perhitungan/', views.index, name="perhitungan/index"),
]
