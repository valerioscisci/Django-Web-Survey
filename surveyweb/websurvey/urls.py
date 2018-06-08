from django.conf.urls import url
from websurvey import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^crossborder/$', views.CrossBorderView.as_view(), name='crossborder'),
    url(r'^crosborder/check_key/', views.check_key, name='check'),
    url(r'^crossborder/save/', views.save, name='save'),
]