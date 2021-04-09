from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home),
    path('list', views.list),
    path('resume', views.resume),
    url(r'^pdf/$', views.GeneratePdf.as_view())
]
