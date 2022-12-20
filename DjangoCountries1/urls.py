from MainApp import (views)
from django.urls import (path)

urlpatterns = [
    path('', views.index),
    path('list_of_countries/page=<int:page>', views.list_of_countries),
    path('list_of_countries/letter=<str:letter>/page=<int:page>', views.seclusion_countries_by_letter),
    path('list_of_countries/letter=<str:letter>', views.seclusion_countries_by_letter),
    path('list_of_languages/', views.list_of_languages),
    path('list_of_languages/<str:language>', views.country_by_languages),
    path('country/<str:country>', views.info_country),
]
