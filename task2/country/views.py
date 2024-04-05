from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from country.models import Country,State,City
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q


class AddCountry(CreateView):
    model=Country
    fields=['country_name']
    template_name='country_create.html'
    success_url = reverse_lazy('home')
class Countries(ListView):
    template_name='home.html'
    model=Country
    def get_queryset(self):
        qs=Country.objects.filter(is_deleted=False)
        return qs
    paginate_by = 3
class UpdateCountry(UpdateView):
    model=Country
    fields=['country_name']
    template_name='country_update.html'
    success_url = reverse_lazy('home')
class DeleteCountry(DeleteView):
    model=Country
    template_name='country_cnfm.html'
    success_url = reverse_lazy('home')
class CountrySearchResults(ListView):
    model = Country
    template_name = 'co_search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get("q")
        object_list = Country.objects.filter(
            Q(country_name__icontains=query)
        )
        return object_list
    success_url=reverse_lazy('co_search_results.html')


class AddState(CreateView):
    model=State
    fields=['state_name','country']
    template_name='state_create.html'
    success_url = reverse_lazy('states_list')
class States(ListView):
    template_name='states_list.html'
    model=State
    def get_queryset(self):
        qss =State.objects.filter(is_deleted=False)
        return qss
    paginate_by = 3
class UpdateState(UpdateView):
    model=State
    fields=['state_name']
    template_name='state_update.html'
    success_url = reverse_lazy('states_list')
class DeleteState(DeleteView):
    model=State
    template_name='state_cnfm.html'
    success_url = reverse_lazy('states_list')
class StateSearchResults(ListView):
    model = State
    template_name = 'st_search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get("q")
        object_list = State.objects.filter(
            Q(state_name__icontains=query)
        )
        return object_list
    success_url=reverse_lazy('st_search_results.html')



class AddCity(CreateView):
    model=City
    fields=['city_name','state','country']
    template_name='city_create.html'
    success_url = reverse_lazy('city_list')
class Cities(ListView):
    template_name='city_list.html'
    model=City
    def get_queryset(self):
        qsc=City.objects.filter(is_deleted=False)
        return qsc
    paginate_by = 3
class UpdateCity(UpdateView):
    model=City
    fields=['city_name']
    template_name='city_update.html'
    success_url = reverse_lazy('city_list')
class DeleteCity(DeleteView):
    model=City
    template_name='city_cnfm.html'
    success_url = reverse_lazy('city_list')
class CitySearchResults(ListView):
    model = City
    template_name = 'ci_search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get("q")
        object_list = City.objects.filter(
            Q(city_name__icontains=query)
        )
        return object_list
    #success_url=reverse_lazy('ci_search_results.html')
