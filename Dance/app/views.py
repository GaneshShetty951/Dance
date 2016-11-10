from datetime import datetime
from time import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render


# Create your views here.
from app.models import UpComingEvents


def main_page(request):
    return render(request, 'home.html', {})

def profile_page(request):
    return render(request, 'profile.html', {})


def upcoming_page(request):
    event_info = UpComingEvents.objects.filter(Q(EventDate__gte = datetime.now())).order_by('EventDate')

    paginator = Paginator(event_info,5)

    page = request.GET.get('page')

    try:
        event_detail = paginator.page(page)
    except PageNotAnInteger:
        event_detail = paginator.page(1)
    except EmptyPage:
        event_detail = paginator.page(paginator.num_pages)

    for event in event_detail:
        print(event.EventImage)
    return render(request, 'upcoming.html', {"event_detail":event_detail})


def recent_page(request):
    event_info = UpComingEvents.objects.filter(Q(EventDate__lte = datetime.now())).order_by('EventDate')
    paginator = Paginator(event_info,3)

    page = request.GET.get('page')

    try:
        event_detail = paginator.page(page)
    except PageNotAnInteger:
        event_detail = paginator.page(1)
    except EmptyPage:
        event_detail = paginator.page(paginator.num_pages)
    return render(request, 'recent.html', {"event_detail":event_detail})