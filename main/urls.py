from django.urls import path
from main import views
urlpatterns = [
    
    path('projects/',views.projects, name='projects'),
    path('skills/',views.skills,name='skills'),
    path('contact/',views.contact,name='contact'),
    path('education/',views.education,name='education'),
    path('achievements/',views.achievements,name='achievements'),
    path('',views.index,name='index'),
    
]