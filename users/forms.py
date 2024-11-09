from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Explicitly define the fields for the custom user creation form
        fields = (
            'username', 'password1', 'password2', 'email',
            'first_name', 'last_name',
            'can_access_contact', 'can_access_sales',
            'can_access_purchase', 'can_access_account'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Explicitly define the fields for the custom user change form
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'can_access_contact', 'can_access_sales',
            'can_access_purchase', 'can_access_account'
        )
