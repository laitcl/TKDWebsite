from django.shortcuts import render
from django.http import HttpResponse
from .models import Instructor, Officer, Alumni, FAQ, Practices, Tournaments, majorfriend, minorfriend

def home(request):
    PageAlumni = Alumni.objects.all()
    PageInstructors = Instructor.objects.filter(page_order__gt=0).order_by('page_order')
    PagePractices = Practices.objects.filter(page_order__gt=0).order_by('page_order')
    context = {'index': True, 'alumni': PageAlumni, 'instructors': PageInstructors, 'practiceslist': PagePractices}
    return render(request, 'tkdwebsite/index.html', context)

def about(request):
    return render(request, 'tkdwebsite/about.html', {'title': 'About'})
    
def calendar(request):
    return render(request, 'tkdwebsite/calendar.html', {'title': 'Calendar'})
    
def contact(request):
    return render(request, 'tkdwebsite/contact.html', {'title': 'Contact'})
    
def faq(request):
    PageFAQs = FAQ.objects.all()
    context = {'title': 'FAQ', 'questions': PageFAQs}
    return render(request, 'tkdwebsite/faq.html', context)

def instructors(request):
    PageInstructors = Instructor.objects.filter(page_order__gt=0).order_by('page_order')
    context = {'title': 'Instructors', 'names': PageInstructors}
    return render(request, 'tkdwebsite/instructors.html', context)

def officers(request):
    PageOfficers = Officer.objects.filter(page_order__gt=0).order_by('page_order')
    context = {'title': 'Officers', 'positions': PageOfficers}
    return render(request, 'tkdwebsite/officers.html', context)

def people(request):
    return render(request, 'tkdwebsite/people.html', {'title': 'People'})

def practices(request):
    PagePractices = Practices.objects.filter(page_order__gt=0).order_by('page_order')
    context = {'title': 'Practices', 'practiceslist': PagePractices}
    return render(request, 'tkdwebsite/practices.html', context)

def social(request):
    return render(request, 'tkdwebsite/social.html', {'title': 'Social'})
    
def tests(request):
    return render(request, 'tkdwebsite/tests.html', {'title': 'Tests'})
    
def tournaments(request):
    PageFallTournaments = Tournaments.objects.filter(semester__startswith='fall').filter(page_order__gt=0).order_by('page_order')
    print(PageFallTournaments)
    PageSpringTournaments = Tournaments.objects.filter(semester__startswith='spring').filter(page_order__gt=0).order_by('page_order')
    PageSummerTournaments = Tournaments.objects.filter(semester__startswith='summer').filter(page_order__gt=0).order_by('page_order')
    context = {'title': 'Practices', 'falltournaments': PageFallTournaments, 'springtournaments': PageSpringTournaments, 'summertournaments': PageSummerTournaments}
    return render(request, 'tkdwebsite/tournaments.html', context)
    
def membersarea(request):
    return render(request, 'tkdwebsite/membersarea.html', {'title': 'Membersarea'})
    
def friends(request):
    PageMajorFriends = majorfriend.objects.filter(page_order__gt=0).order_by('page_order')
    PageMinorFriends = minorfriend.objects.filter(page_order__gt=0).order_by('page_order')
    context = {'title': 'Friends', 'majorfriends': PageMajorFriends, 'minorfriends': PageMinorFriends}
    return render(request, 'tkdwebsite/friends.html', context)

def developer(request):
    return render(request, 'tkdwebsite/developerblog/developer.html', {'title': 'Developer'})
    
def blog1(request):
    return render(request, 'tkdwebsite/developerblog/01.html', {'title': 'Blog1'})

def blog2(request):
    return render(request, 'tkdwebsite/developerblog/02.html', {'title': 'Blog2'})

def blog3(request):
    return render(request, 'tkdwebsite/developerblog/03.html', {'title': 'Blog3'})