from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.home, name='Home'),
    url('about/', views.about, name='About'),
    url('calendar/', views.calendar, name='calendar'),
    url('contact/', views.contact, name='contact'),
    url('faq/', views.faq, name='faq'),
    url('instructors/', views.instructors, name='instructors'),
    url('officers/', views.officers, name='officers'),
    url('people/', views.people, name='people'),
    url('practices/', views.practices, name='practices'),
    url('social/', views.social, name='social'),
    url('tests/', views.tests, name='tests'),
    url('tournaments/', views.tournaments, name='tournaments'),
    url('membersarea/', views.membersarea, name='membersarea'),
    url('friends/', views.friends, name='friends'),
    url('developer/', views.developer, name='developer'),
    url('01/', views.blog1, name='blog1'),
    url('02/', views.blog2, name='blog2'),
    url('03/', views.blog3, name='blog3'),
]
