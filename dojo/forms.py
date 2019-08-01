from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')


def h_validator(value):
    if value != "한결":
        raise forms.ValidationError("본인쟝이 아닙니다")


class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator, h_validator])
    content = forms.CharField(widget=forms.Textarea)
