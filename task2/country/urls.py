from django.urls import path
from .views import AddCountry,Countries,UpdateCountry,DeleteCountry,CountrySearchResults,AddState,States,UpdateState,DeleteState,StateSearchResults,Cities,AddCity,UpdateCity,DeleteCity,CitySearchResults


urlpatterns=[
    path('',Countries.as_view(), name='home'),
    path('home/',AddCountry.as_view(),name='country_create'),
    path('country_update/<int:pk>/',UpdateCountry.as_view(), name='country_update'),
    path('country_cnfm/<int:pk>/',DeleteCountry.as_view(), name='country_delete'),
    path('co_search_results/',CountrySearchResults.as_view(), name='co_search_results'),


    path('state/',States.as_view(), name='states_list'),
    path('state_list/',AddState.as_view(),name='state_create'),
    path('state_update/<int:pk>/',UpdateState.as_view(), name='state_update'),
    path('state_delete/<int:pk>/',DeleteState.as_view(), name='state_delete'),
    path('st_search_results/',StateSearchResults.as_view(), name='st_search_results'),


    path('city/',Cities.as_view(), name='city_list'),
    path('city_list/',AddCity.as_view(),name='city_create'),
    path('city_update/<int:pk>/',UpdateCity.as_view(), name='city_update'),
    path('city_delete/<int:pk>/',DeleteCity.as_view(), name='city_delete'),
    path('ci_search_results/',CitySearchResults.as_view(), name='ci_search_results'),
]

