from django.forms import ModelForm

from django import forms

from .models import Review,Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','featured_image','description','demo_link','source_link']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }


    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input' , 'placeholder':'Add a text'})

class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['value','body']

        labels={'value':'Place your vote:' ,
           'body':'Add a comment for your vote:'}

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input' , 'placeholder':'Add a text'})
                if name=='value':
                    field.widget.attrs.update({'style':'color:blue;'})