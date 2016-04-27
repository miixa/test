from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^subject/$', views.SubjectView),
    url(r'^subject/get/(?P<theme_id>\\d+)/$', views.ThemesView),
]
