from . models import Profile , Skill

from django.db.models import Q

from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage

def profileSearch(request):
    profiles=(Profile.objects.exclude(Q(bio = "") | Q(short_intro = None)))
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    skills=Skill.objects.filter(name__iexact=search_query)

    profiles=profiles.distinct().filter(Q(name__icontains=search_query) | Q(bio__icontains=search_query) | 
                                  Q(short_intro__icontains=search_query) | Q(skill__in=skills) )


    return profiles , search_query 


def profilePagination(request,profiles,result):

    page=request.GET.get('page')
    paginator=Paginator(profiles,result)
    page_range=range(1, (paginator.num_pages+1))

    try:
        profiles=paginator.page(page)

    except PageNotAnInteger:
        page=1
        profiles=paginator.page(page)

    except EmptyPage:
        page=paginator.num_pages
        profiles=paginator.page(page)

    return profiles , page_range