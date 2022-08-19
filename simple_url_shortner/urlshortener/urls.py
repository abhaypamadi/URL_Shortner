from django.conf.urls import url
from django.contrib.auth import views
from .views import register_user, index, redirect

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<short_code>\w+)$', redirect, name='redirect'),

    # auth views
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', register_user, name='register'),
]
