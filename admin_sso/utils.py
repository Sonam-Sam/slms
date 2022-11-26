from documents.models import Document
from django.db.models import QuerySet
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from users.models import Profile
from django.db.models import Q

def paginateDocuments(request, documents, results):
    page = request.GET.get('page')
    paginator = Paginator(documents, results)

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        documents = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        documents = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, documents

def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles

def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(username__icontains=search_query))

    return profiles, search_query

def searchDocuments(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    documents = Document.objects.filter(Q(owner__username__icontains=search_query) | Q(title__icontains=search_query))
    return documents, search_query