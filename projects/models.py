from django.db import models

# Create your models here.
import uuid

class Project(models.Model):
    #owner=models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True, default='default.jpg',upload_to="ProjectImages/")
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)

    tags=models.ManyToManyField('Tag',blank=True)

    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)


    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-vote_ratio' , '-vote_total' , 'title']

class Review(models.Model):
    VOTE_TYPE=( ('UP','UP_VOTE'),( 'DOWN' , 'DOWN_VOTE'))
    #owner=models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)

    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    class Meta:
        ordering=['project','-value' , '-created']

    
    def __str__(self):
        return str(self.project)


class Tag(models.Model):
    name=models.CharField(max_length=400)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name  