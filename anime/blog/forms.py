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
        

class MultiplePostDeleteForm(forms.Form):
    posts = forms.ModelMultipleChoiceField(
        queryset=Post.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control multiple_delete'}),
        required=True,
    )
    
    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', Post.objects.all())
        super().__init__(*args, **kwargs)
        self.fields['posts'].queryset = queryset