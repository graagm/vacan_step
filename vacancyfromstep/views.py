from django.shortcuts import render, redirect
from django.http import Http404
from django.core.handlers.wsgi import WSGIRequest
from .models import Company, Specialty, Vacancy, Rezume
from .forms import Company_forms, Vacancy_forms, Rezume_forms
from django.views.generic.edit import CreateView, UpdateView

from django.db.models import Q


# Create your views here.

def main_index(request):
    companies = Company.objects.all()
    enum_vac = list(Vacancy.objects.filter(company=i).count() for i in Company.objects.all())
    compani = {}
    compan = []
    for i in companies:
        compani.update({'pk': i.pk, 'name': i.name,
                       'location': i.location, 'logo': i.logo, 'description': i.description,
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
    except Company.DoesNotExist:
        raise Http404("DJANGO STEPIK VACANS 404 test")
    companies = Company.objects.get(pk=comp_id)
    vacanci = Vacancy.objects.all().filter(company__pk=comp_id)
    comp_vac_count = vacanci.count()
    return render(request, 'vacancyfromstep/company.html', {'comp_id': comp_id, 'companies': companies,
                  'vacanci': vacanci, 'comp_vac_count': comp_vac_count})


def vacanci_single(request, single_vac=1):
    vacanci_from_single = Vacancy.objects.get(pk=single_vac)
    company_id = vacanci_from_single.company
    return render(request, 'vacancyfromstep/vacancy.html', {'vacanci_from_single': vacanci_from_single,
                                                            'single_vac': single_vac, 'company_id': company_id})


class VacancyCreateView(CreateView):
    template_name = 'vacancyfromstep/new_vacancy.html'
    form_class = Vacancy_forms
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Vacancy'] = Vacancy.objects.all()
        return context


class CompanyCreateView(CreateView):
    template_name = 'vacancyfromstep/new_company.html'
    form_class = Company_forms
    uccess_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Company'] = Company.objects.all()
        return context


class RezumeCreateView(CreateView):
    template_name = 'vacancyfromstep/new_rezume.html'
    form_class = Rezume_forms
    success_url = '/'
    model = Rezume

    def form_valid(self, form):
        rezume_f = form.save(commit=False)
        rezume_f.user = self.request.user
        rezume_f.save()
        return super().form_valid(form)


class RezumeUpdateView(UpdateView):
    form_class = Rezume_forms
    template_name = 'vacancyfromstep/upd_rezume.html'
    success_url = '/'
    model = Rezume
  
    def get_object(self, queryset=None):
        obj = Rezume.objects.get(user=self.request.user)
        return obj


def Rezume_check(request, user_pk):
    rezum_trom = Rezume.objects.all().filter(user__pk=user_pk)
    if rezum_trom:
        return redirect('upd_rezume')
    else:
        return redirect('add_rezume')


def Search(request):
    if request.method == 'POST':
        search_req = request.POST.get("search_req")
        if search_req.strip() == '':
            return redirect('/')
    vacanc_rezult = Vacancy.objects.all().filter(Q(description__icontains=search_req) | Q(title__icontains=search_req))
    count_vac = vacanc_rezult.count()
    return render(request, 'vacancyfromstep/search.html', {'vacanc_rezult': vacanc_rezult, 'count_vac': count_vac})


def Search_quick(request, search_req):
    vacanc_rezult = Vacancy.objects.all().filter(Q(description__icontains=search_req) | Q(title__icontains=search_req))
    count_vac = vacanc_rezult.count()
    if count_vac == 0:
        return redirect('/vacancies/??????_????????????????')
    return render(request, 'vacancyfromstep/search.html', {'vacanc_rezult': vacanc_rezult, 'count_vac': count_vac})
    

