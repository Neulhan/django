from django import forms
from .models import Post


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def save(self, commit=True):
        self.instance = Post(**self.cleaned_data)
        if commit:
            self.instance.save()

        return self.instance

