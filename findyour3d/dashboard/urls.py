from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^company/$', view=views.DashboardView.as_view(), name='company'),
]
