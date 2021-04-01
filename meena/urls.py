from django.urls import path
from meena import views
urlpatterns=[
   path('',views.home),
   path('demo/',views.chk),
   path('ht/',views.homepage,name='home'),
   path('lg/',views.lgn),
   path('rg/',views.reg,name='register'),
   path('hm/',views.bthm),
   path('ab/',views.about,name='about'),
   path('co/',views.contact,name='contact'),
 ]