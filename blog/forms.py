from django import forms
from .models import Post, Comment
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
"""
class ElectricalForm(forms.ModelForm):
	class Meta:
		model = Electrical
		fields = ('title', 'text')

class ElectronicsForm(forms.ModelForm):
	class Meta:
		model = Electronics
		fields = ('title', 'text')
"""