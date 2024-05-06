from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from PIL import Image
from .models import CustomUser, Story


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2')  # Assuming you want to include password confirmation


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('email',)

