from django.urls import path
from .datatables_view import DataPengujianTables
from . import views

urlpatterns = [
    path('detail', views.detail, name="pengujian/detail"),
    path('index_pengujian_data_uji', views.index_pengujian_data_uji, name="pengujian/index_pengujian_data_uji"),
    path('index_pengujian_tunggal', views.index_pengujian_tunggal, name="pengujian/index_pengujian_tunggal"),
    path('pengujian_data_uji', views.pengujian_data_uji, name="pengujian/pengujian_data_uji"),
    path('pengujian_tunggal', views.pengujian_tunggal, name="pengujian/pengujian_tunggal"),
    path('datatable_data_pengujian', DataPengujianTables.as_view(), name="pengujian/datatable_data_pengujian"),
]
