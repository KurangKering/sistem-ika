from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="data-uji/index"),
    path('index', views.index, name="data-uji/index"),
    path('detail', views.detail, name="data-uji/detail"),
    path('insert_or_update', views.insert_or_update, name="data-uji/insert_or_update"),
    path('insert', views.insert, name="data-uji/insert"),
    path('update', views.update, name="data-uji/update"),
    path('delete', views.delete, name="data-uji/delete"),
    path('import_data', views.import_data, name="data-uji/import_data"),
]
