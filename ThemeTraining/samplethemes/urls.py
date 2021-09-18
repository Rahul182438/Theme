from django.urls import path
from .views import CompanySignup, CompanyLogin, CompanyDetail, CompanyPeople, CompanySettings, CompanyTask, CompanyTaskDetail

app_name = 'company'

urlpatterns = [
    path('', CompanySignup.as_view(), name='company-signup'),
    path('login/', CompanyLogin.as_view(), name='company-login'),
    path('company-detail/', CompanyDetail.as_view(), name='company-detail'),
    path('company-people/', CompanyPeople.as_view(), name='company-people'),
    path('company-settings/', CompanySettings.as_view(), name='company-settings'),
    path('company-task/', CompanyTask.as_view(), name='company-task'),
    path('company-task-detail/', CompanyTaskDetail.as_view(), name='company-task-detail'),

]