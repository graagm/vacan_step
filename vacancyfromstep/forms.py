from django.forms import ModelForm
from .models import Company, Specialty, Vacancy


class Company_forms(ModelForm):
     class Meta:
         model = Company;
         fields = ('name', 'location', 'logo', 'description', 'employee_count')


class Specialty_forms(ModelForm):
     class Meta:
         model = Specialty;
         fields = ('code', 'title', 'picture')


class Vacancy_forms(ModelForm):
     class Meta:
         model = Vacancy;
         fields = ('title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max')