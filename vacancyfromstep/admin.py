from django.contrib import admin

# Register your models here.
from .models import Company, Specialty, Vacancy, Rezume


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'logo', 'description', 'employee_count')


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'picture')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'specialty', 'company', 'skills',
                    'description', 'salary_min', 'salary_max', 'published_at')


class RezumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'status',
                    'salary', 'specialty', 'grade', 'education',
                    'experience', 'portfolio',  'published_at')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Rezume, RezumeAdmin)
