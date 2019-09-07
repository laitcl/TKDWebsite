from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    url(r'^', views.home, name='Home'),
    url(r'^about/', views.about, name='About'),
    url(r'^calendar/', views.calendar, name='calendar'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^instructors/', views.instructors, name='instructors'),
    url(r'^officers/', views.officers, name='officers'),
    url(r'^people/', views.people, name='people'),
    url(r'^practices/', views.practices, name='practices'),
    url(r'^social/', views.social, name='social'),
    url(r'^tests/', views.tests, name='tests'),
    url(r'^tournaments/', views.tournaments, name='tournaments'),
    url(r'^membersarea/', views.membersarea, name='membersarea'),
    url(r'^friends/', views.friends, name='friends'),
    url(r'^developer/', views.developer, name='developer'),
    url(r'^01/', views.blog1, name='blog1'),
    url(r'^02/', views.blog2, name='blog2'),
    url(r'^03/', views.blog3, name='blog3'),
)
