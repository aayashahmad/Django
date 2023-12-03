from django.contrib import admin
from django.urls import path, include
from home import views
from .views import contact
# django admin header customization
admin.site.site_header = "Developer Aayash Ahmad"
admin.site.site_title = "Wellcome to Ashu's Dashboard"
admin.site.index_title = "Wellcome to this portal"

urlpatterns = [   
     path('', views.home, name='home'),
     path('about', views.about, name='about'),
     path('projects', views.projects, name='project'),
     path('contact', views.contact, name='contact'),
      path('contact/', contact, name='contact'),

]
