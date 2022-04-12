from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=300)
    employee_count = models.PositiveSmallIntegerField()
 

    class Meta:
        verbose_name = 'наименование компании'
        verbose_name_plural = 'список компаний'


    def __str__(self):
        return self.name



class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.URLField(default='https://place-hold.it/100x60')


    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'список специальностей'


    def __str__(self):
        return self.code


class Vacancy(models.Model):
    title = models.CharField(max_length=20)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'лист вакансий'


    def __str__(self):
        return self.title