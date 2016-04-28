from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^subjects/$', views.SubjectsView),
    url(r'^themes/get/(?P<url_subject_id>\d+)/$', views.ThemesView),
    url(r'^lessons/get/(?P<url_theme_id>\d+)/$', views.LessonsView),
    url(r'^lesson/get/(?P<url_lesson_id>\d+)/$', views.LessonView),
]
