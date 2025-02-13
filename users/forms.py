from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    """Form for user registration with username, email, and password validation."""

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}),
        max_length=50, required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """Ensure the email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already taken. Please choose another.")
        return email

    def clean_username(self):
        """Ensure the username is unique."""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken. Please choose another.")
        return username

    def clean(self):
        """Ensure both password fields match."""
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    """Form to allow users to update their username and email with consistent styling."""

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}),
        max_length=50, required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}), required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}), required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        """Ensure both password fields match if they are provided."""
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


class ProfileUpdateForm(forms.ModelForm):
    """Form to allow users to update their profile details with consistent styling."""

    profile_picture = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'prompt srch_explore'}), required=False
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write something about yourself...', 'class': 'prompt srch_explore', 'rows': 3}),
        required=False
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your location', 'class': 'prompt srch_explore'}),
        required=False
    )
    skills = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Skills (comma-separated)', 'class': 'prompt srch_explore'}),
        required=False
    )
    website = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder': 'Your website', 'class': 'prompt srch_explore'}),
        required=False
    )
    github = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder': 'GitHub Profile', 'class': 'prompt srch_explore'}),
        required=False
    )
    resume = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'prompt srch_explore'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'location', 'skills', 'website', 'github', 'resume']
