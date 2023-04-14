from .models import Project,Tag

from django.db.models import Q

from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage

def projectSearch(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    tags=Tag.objects.filter(name__icontains=search_query)

    projects=Project.objects.distinct().filter(Q(title__icontains=search_query) | Q(vote_total__icontains=search_query) |
                            Q(tags__in=tags) | Q(owner__username__icontains=search_query))

    return projects , search_query


def projectPagination(request,projects,result):

    page=request.GET.get('page')
    paginator=Paginator(projects,result)
    page_range=range(1, (paginator.num_pages+1))

    try:
        projects=paginator.page(page)

    except PageNotAnInteger:
        page=1
        projects=paginator.page(page)

    except EmptyPage:
        page=paginator.num_pages
        projects=paginator.page(page)

    leftIndex= int(page) - 4
    if leftIndex < 1:
        leftIndex=1

    rightIndex= int(page) + 6
    if rightIndex > paginator.num_pages:
        rightIndex=paginator.num_pages + 1

    custom_range=range(leftIndex,rightIndex)

    showFirstPage=False
    showLastPage=False

    if paginator.num_pages > rightIndex - 1 :
        showLastPage=True

    if leftIndex>1:
        showFirstPage=True

    return projects , custom_range , showFirstPage , showLastPage