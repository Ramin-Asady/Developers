from .models import Project,Tag

from django.db.models import Q

def projectSearch(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    tags=Tag.objects.filter(name__icontains=search_query)

    projects=Project.objects.distinct().filter(Q(title__icontains=search_query) | Q(vote_total__icontains=search_query) |
                            Q(tags__in=tags) | Q(owner__username__icontains=search_query))

    return projects , search_query