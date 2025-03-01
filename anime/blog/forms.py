from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tên nội dung'
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Viết nội dung cần gửi của bạn...'
                }),
            'image': forms.FileInput(attrs={
                'class': 'form-control file_input',
                })
        }