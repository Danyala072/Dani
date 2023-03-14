from django import forms

from .models import Comment, Contact

class CommentForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control w-25', 'placeholder':'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control w-25', 'placeholder':'Email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-50', 'rows':'3', 'cols':'10' , 'placeholder':'Message'}))
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
class ContactForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control w-25', 'placeholder':'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control w-25', 'placeholder':'Email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-50', 'rows':'3', 'cols':'10' , 'placeholder':'Message'}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']