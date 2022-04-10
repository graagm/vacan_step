from django.shortcuts import render
from django.http import Http404
from django.core.handlers.wsgi import WSGIRequest
from .models import Company, Specialty, Vacancy


# Create your views here.

def main_index(request):
    companies = Company.objects.all()
    enum_vac = list(Vacancy.objects.filter(company=i).count() for i in Company.objects.all())
    compani = {}
    compan = []
    for i in companies:
        compani.update({'pk': i.pk, 'name': i.name, 'location': i.location, 'logo': i.logo, 'description': i.description,
                       'employee_count': i.employee_count, 'count': enum_vac[i.pk-1]})
        compan.append(compani)
        compani = {}
    specialt = Specialty.objects.all()
    enum_spec = list(Vacancy.objects.filter(specialty=i).count() for i in Specialty.objects.all())
    special = {}
    spec = []
    for i in specialt:
        special.update({'pk': i.pk, 'code': i.code, 'title': i.title, 'picture': i.picture, 'count': enum_spec[i.pk-1]})
        spec.append(special)
        special = {}
    return render(request, 'vacancyfromstep/index.html', {'compan': compan, 'spec': spec})


def vacanci_values(request, cat=None):
    vacanci_from_cat = Vacancy.objects.all().filter(specialty__code=cat)
    vacanci_all = Vacancy.objects.all()
    count_vac = vacanci_from_cat.count()
    return render(request, 'vacancyfromstep/vacancies.html', {'cat':
                  cat, 'vacanci_from_cat': vacanci_from_cat, 'count_vac': count_vac, 'vacanci_all': vacanci_all})


def comp_values(request: WSGIRequest, comp_id=None):
    try:
        c_obj = Company.objects.get(pk=comp_id)
    except KeyError:
        raise Http404
    companies = Company.objects.get(pk=comp_id)
    vacanci = Vacancy.objects.all().filter(company__pk=comp_id)
    comp_vac_count = vacanci.count()
    return render(request, 'vacancyfromstep/company.html', {'comp_id': comp_id, 'companies': companies,
                  'vacanci': vacanci, 'comp_vac_count': comp_vac_count})


def vacanci_single(request, single_vac=1):
    vacanci_from_single = Vacancy.objects.get(pk=1)
    return render(request, 'vacancyfromstep/vacancy.html', {'vacanci_from_single': vacanci_from_single})
