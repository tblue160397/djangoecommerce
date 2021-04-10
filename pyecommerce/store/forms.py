from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email']
        widgets = {
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': forms.fields.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'username': forms.fields.TextInput(attrs={'placeholder': 'Enter your user name', 'class': 'form-control'}),
            'password1': forms.fields.TextInput(attrs={'placeholder': 'Enter your password name', 'class': 'form-control'}),
            'password2': forms.fields.TextInput(attrs={'placeholder': 'Enter your confirm password like password', 'class': 'form-control'}),
            'email': forms.fields.EmailInput(attrs={'placeholder': 'Enter your Email', 'class': 'form-control'}),
        }

        def save(self, commit=True):
            user = super(CustomerForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user