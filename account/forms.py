from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            'password': forms.PasswordInput()
        }

    # ✅ username check
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username already used")
        return username

    # ✅ email check
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email already used")
        return email

    # 🔥 IMPORTANT: password match check
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if not confirm_password:
            raise forms.ValidationError("Confirm password is required")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data