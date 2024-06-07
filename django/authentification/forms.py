from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check for existing email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email