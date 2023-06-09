from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProjectSerializer , ProfileSerializer
from projects.models import Project, Review
from users.models import Profile

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def getProject(request,pk):

       project=Project.objects.get(id=pk)
       serializer=ProjectSerializer(project, many=False)
       return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfiles(request):

       profiles=Profile.objects.all()
       serializer=ProfileSerializer(profiles, many=True)
       return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request,pk):

       userProfile=Profile.objects.get(id=pk)
       serializer=ProfileSerializer(userProfile, many=False)
       return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
      project=Project.objects.get(id=pk)
      user=request.user.profile
      data=request.data
      review , created =Review.objects.get_or_create(
            owner=user,
            project=project,

      )
      review.body=data['body']
      review.value=data['value']
      review.save()
      project.getVoteCount
    
      content={
            "Status" : "Your review submitted or in the case of having review on this Project it is modified"
      }
      return Response(content)

