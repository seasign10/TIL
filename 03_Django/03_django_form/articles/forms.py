from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10, 
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': 'Enter the title',
#             }
#         )
#     )
#     # max_length를 지정하지 않으면 텍스트 필드로 사용이가능하다.
#     # model과는 달리 form에는 text field가 없다.
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         )
#     )

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Article # 이 모델을 통해 form을 만들면 되겠다는 명령
        # fields = ('title', 'content',)
        fields = ('title', 'content',)
        # exclude = ('title',) # title을 제외한 모든 필드를 사용

        # 
        # wigets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'
        #     })
        # }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)