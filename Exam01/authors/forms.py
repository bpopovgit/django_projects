from django import forms
from .models import Author


class CreateAuthorForm(forms.ModelForm):
    passcode = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter 6 digits...',
            'aria-describedby': 'id_passcode_helptext'
        }),
        help_text="Your passcode must be a combination of 6 digits",
        label="Passcode:"
    )

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }


class EditAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:',
        }
        widgets = {
            'info': forms.Textarea(attrs={'placeholder': 'Tell us more about yourself...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter a link to your profile image...'}),
        }