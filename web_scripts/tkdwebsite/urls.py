from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('calendar/', views.calendar, name='calendar'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('instructors/', views.instructors, name='instructors'),
    path('officers/', views.officers, name='officers'),
    path('people/', views.people, name='people'),
    path('practices/', views.practices, name='practices'),
    path('social/', views.social, name='social'),
    path('tests/', views.tests, name='tests'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('membersarea/', views.membersarea, name='membersarea'),
    path('friends/', views.friends, name='friends'),
    path('developer/', views.developer, name='developer'),
    path('01/', views.blog1, name='blog1'),
    path('02/', views.blog2, name='blog2'),
    path('03/', views.blog3, name='blog3'),
]
