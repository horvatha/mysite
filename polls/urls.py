from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^[A-Z]{3}-[0-9]{3}$', views.rendszam, name="rendszam")
]


""" 1.7.x
from django.conf.urls import url, patterns
urlpatterns = patterns("",
    url(r'^[A-Z]{3}-[0-9]{3}$', views.rendszam, name="rendszam")
)
"""
