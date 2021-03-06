"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from vacancyfromstep.views import main_index, vacanci_values
from vacancyfromstep.views import comp_values, vacanci_single, VacancyCreateView
from vacancyfromstep.views import CompanyCreateView, RezumeCreateView, Rezume_check
from vacancyfromstep.views import RezumeUpdateView, Search, Search_quick


urlpatterns = [
   path('', main_index, name='main_index'),
   path('vacancies/<int:single_vac>', vacanci_single, name='vacanci_single'),
   path('add/vacancie', VacancyCreateView.as_view(), name='add_vacancie'),
   path('add/company', CompanyCreateView.as_view(), name='add_company'),
   path('add/rezume/<int:user_pk>', Rezume_check, name='check_rezume'),
   path('add/rezume/', RezumeCreateView.as_view(), name='add_rezume'),
   path('rezume/edit', RezumeUpdateView.as_view(), name='upd_rezume'),
   path('search/', Search, name='search'),
   path('search/<slug:search_req>', Search_quick, name='search_quick'),
   re_path('vacancies/company/?(?P<comp_id>\d{1,3})?', comp_values, name='vac_comp_values'),
   re_path('companies/?(?P<comp_id>\d{1,3})?', comp_values, name='comp_values'),
   re_path('vacancies/?(?P<cat>\w{6,15})?', vacanci_values, name='vacanci_values'),
]
