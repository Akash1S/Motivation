from django.conf.urls import url
from service import views
urlpatterns = [
    url(r'^Details/', views.d_details, name='pulak'),
    url(r'^Seminars/', views.seminar, name='seminars_gallery'),
    url(r'^Course/', views.course_name, name='courses'),
    url(r'^about_us/', views.contact_us, name='about_us'),

]
