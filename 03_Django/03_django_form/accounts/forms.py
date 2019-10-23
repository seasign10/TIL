from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # return 값이 User
        fields = ('email', 'last_name', 'first_name',)

class CustomUserCreationForm(UserCreationForm):
    # class Meta:
    #     model = get_user_model()
    #     fields = ('username', 'password1', 'password2', 'password3')
    class Meta(UserCreationForm): # UserCreationForm 의 Meta를 상속 받을 수 있음
        # model은 이미 가지고 있기 때문에 생략 가능,
        model = get_user_model() #accounts.user
        fields = UserCreationForm.Meta.fields + ('email',)
        # UserCreationForm의 Meta에 있는 fields + ...
