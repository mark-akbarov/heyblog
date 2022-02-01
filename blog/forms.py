from django import forms
from .models import BlogComment

class BlogCommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':2,
        'cols':50
    }))
    class Meta:
        model = BlogComment
        fields =['content']