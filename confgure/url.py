from django.urls import path
from jobs.views import job_list

urlpatterns = [
    path('', job_list, name='home'),
]