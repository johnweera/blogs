from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import Post


# class PostForm(forms.Form):
#     post_name = forms.CharField(max_length=100)
#     post_detail = forms.CharField(widget=forms.Textarea, max_length=1000)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_name', 'post_detail']
        widgets = {
            'post_name':TextInput(attrs={'class':'ql-editor ql-container ql-snow', 'size':'60'}),
            'post_detail':Textarea(attrs={'id':'editor2'}),
        }