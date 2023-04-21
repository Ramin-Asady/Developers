from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProjectSerializer , ProfileSerializer
from projects.models import Project
from users.models import Profile

@api_view(['GET'])
def getRoutes(request):

    routes=[
           {'GET':'http://127.0.0.1:8000/API/projects'},
           {'GET':'http://127.0.0.1:8000/API/projects/singleProject.id'},

           {'GET':'http://127.0.0.1:8000/API/profiles'},
           {'GET':'http://127.0.0.1:8000/API/profiles/userProfile.id'},
    ]

    return Response(routes)


@api_view(['GET'])
def getProjects(request):

       projects=Project.objects.all()
       serializer=ProjectSerializer(projects, many=True)
       return Response(serializer.data)


@api_view(['GET'])
def getProject(request,pk):

       project=Project.objects.get(id=pk)
       serializer=ProjectSerializer(project, many=False)
       return Response(serializer.data)

@api_view(['GET'])
def getProfiles(request):

       profiles=Profile.objects.all()
       serializer=ProfileSerializer(profiles, many=True)
       return Response(serializer.data)

@api_view(['GET'])
def getUserProfile(request,pk):

       userProfile=Profile.objects.get(id=pk)
       serializer=ProfileSerializer(userProfile, many=False)
       return Response(serializer.data)

