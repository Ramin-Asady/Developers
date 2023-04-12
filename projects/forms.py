from django.forms import ModelForm

from django import forms

from .models import Review

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