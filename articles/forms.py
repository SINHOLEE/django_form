from django import forms

# 사용자에게 입력받는 Field만 작성
class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label= '젬옥',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '제목을 입력하세요.',
            }
        ),
    )
    content = forms.CharField(
        label='내옹',
        widget=forms.Textarea(
            attrs={
                'placeholder' : '내용을 입력하세요.',
                'row' : 5,
                'col' : 50,
            }
        ),
    )