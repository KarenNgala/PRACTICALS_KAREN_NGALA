from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^create_stream/$', views.create, name='create_stream'),
    url(r'^create_student/$', views.create_student, name='create_student'),
    url(r'^student/(\d+)/$', views.student_deets, name='student_details'),
    url(r'^edit/(\d+)/$', views.edit_student, name='edit_student'),
    url(r'^students/(\d+)/$', views.all_students, name='view_students'),
    url(r'^delete/(\d+)/$', views.delete_student, name='delete_student'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)