from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new_bunk$', views.CreateBunkView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w\d]+)$', views.UserProfileView.as_view(), name='detail'),
]
