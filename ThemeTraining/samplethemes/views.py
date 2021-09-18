from django.shortcuts import render
from django.views.generic.base import TemplateView


class CompanySignup(TemplateView):
    template_name = "registration/company-signup.html"

class CompanyLogin(TemplateView):
    template_name = "registration/company-login.html"

class CompanyDetail(TemplateView):
    template_name = "company_info/company-detail.html"

class CompanyPeople(TemplateView):
    template_name = "company_info/company-people.html"

class CompanySettings(TemplateView):
    template_name = "company_info/company-settings.html"

class CompanyTask(TemplateView):
    template_name = "company_info/company-task.html"

class CompanyTaskDetail(TemplateView):
    template_name = "company_info/company-task-detail.html"
