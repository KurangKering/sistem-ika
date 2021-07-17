from django.urls import path

from . import views

urlpatterns = [
    path('detail', views.detail, name="pengujian/detail"),
    path('pengujian_data_uji', views.pengujian_data_uji, name="pengujian/pengujian_data_uji"),
    path('pengujian_tunggal', views.pengujian_tunggal, name="pengujian/pengujian_tunggal"),
]
