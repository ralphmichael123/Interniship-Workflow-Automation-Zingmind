from django.conf.urls import urls
from account import views

urlpatterns=[
    urls(r'^account$',views.registrationapi),
    urls(r'^account/([0-9]+)$')
]