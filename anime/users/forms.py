from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class CustomLoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)  # Dùng authenticate()
            if user is None:
                raise forms.ValidationError("Email hoặc mật khẩu không đúng")
            self.user = user  # Lưu user để lấy trong get_user()

        return self.cleaned_data

    def get_user(self):
        return getattr(self, "user", None)  # Trả về user đã authenticate